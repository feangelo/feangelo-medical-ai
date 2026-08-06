# Data Governance

## Absolute prohibition

Private clinical DICOM, identifiable medical images, protected health information, re-identification keys, and restricted data must never be committed to this repository.

## Allowed classifications

Every case must declare exactly one classification in `case.yaml`:

| Classification | Meaning | Minimum evidence |
|---|---|---|
| `synthetic` | Artificial data not derived from an identifiable individual. | Generation method and limitations. |
| `open-dataset` | Data obtained from a documented open dataset. | Source URL, dataset version, license, and citation. |
| `public` | Data already lawfully public and permitted for redistribution. | Provenance, rights assessment, and access date. |

Classification is mandatory but not sufficient. A manual review must also confirm that the files are safe, licensed, necessary, and free of identifiers.

## Publication checklist

Before any data-derived asset is committed:

1. Confirm classification and provenance.
2. Review the source license and redistribution terms.
3. Inspect pixels, headers, filenames, overlays, screenshots, and metadata.
4. Remove credentials and local paths.
5. Confirm that no linkage or re-identification material is present.
6. Record the reviewer, date, decision, and limitations.
7. Prefer download instructions and checksums over committing datasets.

## Git safeguards

The `.gitignore` denies common medical-image, volume, mesh, model, archive, and media formats by default. These patterns are a safety layer, not a guarantee. Any exception requires a documented review and a narrowly scoped negation rule.

## Incident handling

If prohibited data are found, stop. Do not publish, duplicate, or run automated cleanup. Preserve relevant context securely, notify the owner through a private channel, and follow applicable institutional procedures.

