"""Validate SEO and crawlability of the built MkDocs site."""

from __future__ import annotations

import json
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

SITE_URL = "https://feangelo.github.io/feangelo-medical-ai/"
SITEMAP_NAMESPACE = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


class PageParser(HTMLParser):
    """Collect SEO-relevant elements from one HTML document."""

    def __init__(self) -> None:
        super().__init__()
        self.canonical: list[str] = []
        self.descriptions: list[str] = []
        self.h1_count = 0
        self.json_ld: list[str] = []
        self.links: list[str] = []
        self.meta: dict[tuple[str, str], str] = {}
        self.title_parts: list[str] = []
        self._capture_title = False
        self._capture_json_ld = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = {key: value or "" for key, value in attrs}
        if tag == "link" and attributes.get("rel") == "canonical":
            self.canonical.append(attributes.get("href", ""))
        elif tag == "meta":
            key = attributes.get("name") or attributes.get("property")
            if key:
                self.meta[("meta", key)] = attributes.get("content", "")
            if attributes.get("name") == "description":
                self.descriptions.append(attributes.get("content", ""))
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "a" and attributes.get("href"):
            self.links.append(attributes["href"])
        elif tag == "title":
            self._capture_title = True
        elif tag == "script" and attributes.get("type") == "application/ld+json":
            self._capture_json_ld = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._capture_title = False
        elif tag == "script":
            self._capture_json_ld = False

    def handle_data(self, data: str) -> None:
        if self._capture_title:
            self.title_parts.append(data)
        elif self._capture_json_ld:
            self.json_ld.append(data)

    @property
    def title(self) -> str:
        return "".join(self.title_parts).strip()


def public_html_files(site_dir: Path) -> list[Path]:
    """Return index pages represented in the sitemap, excluding technical HTML files."""
    return sorted(
        path
        for path in site_dir.rglob("*.html")
        if path.name == "index.html" and path.parent.name != "404"
    )


def path_url(path: Path, site_dir: Path) -> str:
    relative = path.relative_to(site_dir).as_posix()
    relative = relative.removesuffix("index.html")
    return urljoin(SITE_URL, relative)


def local_target_exists(href: str, source_url: str, site_dir: Path) -> bool:
    parsed = urlparse(urljoin(source_url, href))
    if parsed.netloc != urlparse(SITE_URL).netloc:
        return True
    site_path = parsed.path.removeprefix("/feangelo-medical-ai/")
    site_path = unquote(site_path)
    candidate = site_dir / site_path
    if candidate.is_dir() or not candidate.suffix:
        candidate /= "index.html"
    return candidate.is_file()


def validate(site_dir: Path) -> tuple[int, int]:
    """Validate the built site and return HTML and sitemap URL counts."""
    errors: list[str] = []
    public_pages = public_html_files(site_dir)
    parsed_pages: dict[str, PageParser] = {}

    for html_file in public_pages:
        page_url = path_url(html_file, site_dir)
        parser = PageParser()
        parser.feed(html_file.read_text(encoding="utf-8"))
        parsed_pages[page_url] = parser
        if parser.canonical != [page_url]:
            errors.append(f"{page_url}: canonical mismatch {parser.canonical!r}")
        if len(parser.descriptions) != 1 or not parser.descriptions[0].strip():
            errors.append(f"{page_url}: requires one non-empty meta description")
        if not parser.title:
            errors.append(f"{page_url}: missing title")
        if parser.h1_count != 1:
            errors.append(f"{page_url}: expected one h1, found {parser.h1_count}")
        for required_meta in (
            "og:type",
            "og:site_name",
            "og:title",
            "og:description",
            "og:url",
            "twitter:card",
            "twitter:title",
            "twitter:description",
        ):
            if not parser.meta.get(("meta", required_meta)):
                errors.append(f"{page_url}: missing {required_meta}")
        robots = parser.meta.get(("meta", "robots"), "").lower()
        if "noindex" in robots or "nofollow" in robots:
            errors.append(f"{page_url}: unexpected robots directive {robots!r}")
        for payload in parser.json_ld:
            try:
                structured_data = json.loads(payload)
            except json.JSONDecodeError as error:
                errors.append(f"{page_url}: invalid JSON-LD: {error}")
                continue
            if structured_data.get("@context") != "https://schema.org":
                errors.append(f"{page_url}: JSON-LD has an invalid @context")
        for href in parser.links:
            if href.startswith(("mailto:", "tel:", "javascript:")) or href.startswith("#"):
                continue
            if not local_target_exists(href, page_url, site_dir):
                errors.append(f"{page_url}: broken internal link {href!r}")

    titles = [page.title for page in parsed_pages.values()]
    if len(titles) != len(set(titles)):
        errors.append("Public page titles are not unique")

    sitemap_path = site_dir / "sitemap.xml"
    sitemap_root = ET.parse(sitemap_path).getroot()
    sitemap_urls = [
        element.text or "" for element in sitemap_root.findall("sm:url/sm:loc", SITEMAP_NAMESPACE)
    ]
    expected_urls = sorted(parsed_pages)
    if sorted(sitemap_urls) != expected_urls:
        errors.append("Sitemap URLs do not exactly match public index pages")
    if any(not url.startswith(SITE_URL) for url in sitemap_urls):
        errors.append("Sitemap contains a non-canonical or relative URL")

    robots = (site_dir / "robots.txt").read_text(encoding="utf-8")
    if "Allow: /" not in robots or f"Sitemap: {SITE_URL}sitemap.xml" not in robots:
        errors.append("robots.txt does not allow crawling or advertise the canonical sitemap")
    if "Disallow:" in robots:
        errors.append("robots.txt contains an unexpected Disallow directive")

    home_json_ld = parsed_pages[SITE_URL].json_ld
    about_json_ld = parsed_pages[f"{SITE_URL}about/"].json_ld
    if len(home_json_ld) != 1 or json.loads(home_json_ld[0]).get("@type") != "WebSite":
        errors.append("Home requires one WebSite JSON-LD object")
    if len(about_json_ld) != 1:
        errors.append("About requires one ProfilePage JSON-LD object")
    else:
        profile = json.loads(about_json_ld[0])
        if (
            profile.get("@type") != "ProfilePage"
            or profile.get("mainEntity", {}).get("@type") != "Person"
        ):
            errors.append("About JSON-LD requires ProfilePage with Person mainEntity")

    if errors:
        print("Site validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)

    print(f"Validated {len(public_pages)} public HTML pages and {len(sitemap_urls)} sitemap URLs.")
    return len(public_pages), len(sitemap_urls)


if __name__ == "__main__":
    validate(Path(sys.argv[1] if len(sys.argv) > 1 else "site"))
