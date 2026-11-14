# AWS Certified Solutions Architect – Associate (SAA-C03) Study Guide

Personal study notes, condensed revision sheets and practice questions for the AWS SAA-C03 exam, published as a searchable website.

**Site:** https://dlamott.github.io/aws_saa_c03_study_guide/

## What's inside

All source content lives in `content/`.

| Folder | Contents |
|---|---|
| `content/notes/` | Full course notes, one file per chapter (IAM, EC2, S3, VPC, serverless, databases, DR, and more), plus a "Key Matches" cheat sheet |
| `content/handnotes/` | Short per-chapter summaries for quick revision, including a service key-mapping sheet |
| `content/waf/` | Well-Architected Framework: overview, the pillars, how to run a review, with transcripts (PDF) |
| `content/mcq/` | Multiple-choice practice questions with answers and explanations, grouped three ways |

Practice questions (`content/mcq/`):

- `section-based/`: one file per exam domain (Resilient, High-Performing, Secure, Cost-Optimized)
- `topic-based/`: one file per service (EC2, S3, VPC, Lambda, and others)
- `review_mode/` and `tm/`: extra question sets
- `SAA_MCQ.md`: a general mixed set

Each answer is in a collapsible block, so you can try the question before revealing it.

## Suggested way to use it

1. Read the chapter in `notes/`, or the matching summary in `handnotes/` if you're revising.
2. Do the `topic-based` questions for that service.
3. Before the exam, work through the `section-based` sets and re-read Key Matches.

## Running the site locally

Requires Python 3.

```bash
pip install -r requirements.txt
mkdocs serve        # http://127.0.0.1:8000, live reload
mkdocs build --strict   # build to ./site and fail on broken links
```

## Project layout

```
content/            site source (markdown, images, PDFs)
mkdocs.yml          site config and sidebar navigation
hooks/              small MkDocs hook so markdown renders inside <details> answer blocks
requirements.txt    pinned MkDocs dependencies
.github/workflows/  GitHub Actions workflow that deploys to GitHub Pages
```

## Editing content

- Add or edit markdown under `content/`. Images go in the `img/` folder next to the notes that use them and are linked with relative paths.
- New pages must be added to the `nav:` section of `mkdocs.yml` to appear in the sidebar.
- Pushing to `main` rebuilds and redeploys the site automatically (Pages source must be set to **GitHub Actions** in the repo settings).

## Notes

- Some answers were corrected against current AWS behaviour (for example Aurora Serverless v1 vs v2). Corrections are marked in the question files.
- These are personal study notes and are not affiliated with or endorsed by AWS.
