# Technical SEO Phase 2 Report

**Date:** 2026-08-22

**Site:** <https://feangelo.github.io/feangelo-medical-ai/>

**Scope:** crawlability, page metadata, structured data, internal discovery, and build validation

## Initial audit: 13 questions

1. **Generated HTML:** the clean baseline contained 14 HTML files. Twelve were public content
   pages; the other two were the 404 page and Google Search Console verification file.
2. **Sitemap coverage:** the baseline sitemap listed Home, About, Architecture, Case Standard,
   Data Governance, Development, Learning, Research Notes, Roadmap, Vision, Work, and Wiki.
3. **Sitemap URLs:** all 12 entries were absolute HTTPS URLs under the configured canonical
   `site_url`.
4. **Robots:** no `robots.txt` was present in the source or baseline build.
5. **Indexing directives:** public content pages had correct canonical links and no `noindex`,
   `nofollow`, or accidental crawl block. The technical 404 behavior is not treated as a public
   content page.
6. **Crawlable internal links:** the MkDocs pages were linked with HTML anchors, but all 14 Lesson
   links left the site for the GitHub source view. The Lessons had no HTML pages on the portfolio.
7. **Navigation paths:** the main navigation covered the principal sections and Home linked to
   Work and Learning. The public site offered no internal navigation path to an HTML Lesson page.
8. **Titles and descriptions:** MkDocs generated unique titles and correct headings. Every page
   reused the same site-wide description instead of a page-specific description.
9. **Social and structured metadata:** canonical links existed. Open Graph, Twitter Card, and
   JSON-LD metadata did not.
10. **JavaScript dependency:** important content was server-rendered in HTML; JavaScript was not
    required to discover or read it.
11. **Broken, duplicate, and orphan pages:** no broken local links were found in the baseline
    content set. There were no duplicate canonical URLs. The canonical Lesson sources were outside
    the public build and therefore absent from the site graph and sitemap.
12. **Person and identity:** visible content associated Felipe Angelo with FAMAI Lab, but no
    machine-readable Person/ProfilePage/WebSite relationship existed.
13. **Why only Home was indexed:** Search Console's reported state is compatible with a recently
    discovered small site and is not proof of an error. The missing public Lesson pages, generic
    descriptions, absence of robots sitemap discovery, and comparatively shallow internal content
    graph reduced additional discovery signals. Google still decides crawl and indexing timing.

## Implemented changes

- The 14 canonical files in `learning/3d-slicer/` are exposed as virtual MkDocs pages during the
  build. No duplicate Lesson copy is maintained in `docs/`, and the canonical scientific text was
  not edited.
- The Learning index and site navigation now use crawlable internal links to those Lesson pages.
- Page-specific, evidence-bounded descriptions are assigned to all public content pages.
- Every public page receives canonical, Open Graph, and summary Twitter Card metadata. No social
  image was added because the repository contains no appropriate confirmed image asset.
- `robots.txt` explicitly permits crawling and advertises the absolute sitemap URL.
- Home receives `WebSite` JSON-LD. About receives `ProfilePage` JSON-LD whose `mainEntity` is
  `Person` for Felipe Angelo. The WebSite references the Person as creator; no Organization object
  is asserted.
- `sameAs` contains only the GitHub and LinkedIn profiles already published consistently in the
  repository. YouTube, Instagram, TikTok, Facebook, and other profiles remain unlinked pending
  explicit confirmation.
- The HTML language remains English (`lang="en"`) and all existing URLs remain unchanged. New
  Lesson URLs are under `/lessons/<existing-lesson-slug>/`.
- A standard-library validator now checks HTML metadata, headings, canonical URLs, internal links,
  JSON-LD syntax/basic semantics, sitemap parity, robots directives, and crawl blocks. Quality and
  Pages workflows run it after the strict build.

## Build inventory

The updated clean build generates **28 HTML files total**:

- **26 public content pages**, all included in `sitemap.xml`;
- one technical `404.html`;
- one Google Search Console verification HTML file.

The sitemap includes the original 12 content URLs plus the 14 stable Lesson URLs. All entries are
absolute canonical HTTPS URLs.

## Structured data and identity boundaries

- **Home:** one `WebSite` object, named `Felipe Angelo Medical AI Lab`, alternate name `FAMAI Lab`,
  with Felipe Angelo's Person identifier as creator.
- **About:** one `ProfilePage` object with a `Person` main entity, general location São Paulo,
  Brazil, and carefully qualified areas of knowledge/learning.
- **Confirmed `sameAs`:** <https://github.com/feangelo> and
  <https://www.linkedin.com/in/felipe-angelo-1812a985>.
- **Not asserted:** formal Organization status, profile image, Twitter/X identity, or any
  unconfirmed social profile.

## Validation evidence

Executed with the project's declared Python 3.12 toolchain:

```text
python -m mkdocs build --strict
python scripts/validate_site.py site
python -m ruff check .
python -m ruff format --check .
python -m pytest
```

The first post-change build exposed a template edge case on the 404 page; the override was guarded
for non-content pages, then the full validation sequence was repeated. The final local results were:

- strict MkDocs build: passed;
- SEO/crawlability validator: 26 public pages and 26 sitemap URLs passed;
- Ruff lint and format check: passed;
- pytest: 5 passed;
- desktop responsive check at 1280 px: no horizontal overflow; primary navigation present;
- mobile checks at 390 × 844 px: no horizontal overflow on Home or Lesson 14; menu control and
  primary Home actions remained visible;
- no public content page contains `noindex` or `nofollow`.

## Limitations and manual follow-up

- Valid structured data does not guarantee a Google rich result or indexing.
- External profile availability and Google's rendered interpretation require public post-deploy
  checks; Search Console data cannot be changed or predicted by this repository.
- After deployment, submit or resubmit
  `https://feangelo.github.io/feangelo-medical-ai/sitemap.xml` in Google Search Console, inspect Home,
  About, Learning, and a representative Lesson URL, request indexing only where appropriate, and
  monitor the Pages indexing and Sitemaps reports over time.
- Confirm additional official social profiles before adding any future `sameAs` URL.
