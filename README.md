# MGT 816 Fall 2026 — Course Website

Public course hub for **The Private Firm CFO: Accounting and Finance Strategies** (Yale SOM, Fall-1 2026).

**Live site:** https://barrios88.github.io/mgt816-fall2026/

Canvas remains the system of record for graded work, licensed cases, and problem sets.

## First-time setup (maintainer)

1. **Enable GitHub Pages:** Repo → Settings → Pages → Build and deployment → **GitHub Actions**
2. Push to `main` — the `publish.yml` workflow builds and deploys automatically
3. Replace `CANVAS_URL_PLACEHOLDER` in `_quarto.yml`, `index.qmd`, and `course-info.qmd`
4. Add `files/syllabus.pdf` (compile from Overleaf `Syllabus_Overleaf/main.tex`)

### Local preview (optional)

```bash
brew install --cask quarto
pip install pyyaml pandas tabulate
quarto render
quarto preview
```

**PS1 workbench:** edits live in `ps1/index.html`. `quarto preview` serves the copy in `_site/ps1/` — after changing the workbench, run `cp ps1/index.html _site/ps1/index.html` (or `quarto render`) before refreshing the browser.

## Weekly routine (5 minutes, after the 4:10 section)

1. Export student slide deck → `materials/sNN_slides.pdf`
2. Edit `schedule.yml`: set `slides:` (and `handouts:` if any)
3. Update the "This week" block on `index.qmd`
4. On case days: update `cases.qmd` links from locked → live
5. Commit and push — site updates in ~2 minutes

## Content policy (the stranger test)

**If you would hand it to a stranger at a conference, it goes on the site.**

| ✅ Public | ❌ Never in repo |
|:----------|:-----------------|
| Scrubbed student slide PDFs | Problem set solutions |
| Syllabus PDF | Grading rubrics / TA guides |
| AI toolkit (prompts, ground rules) | HBS case PDFs |
| Cap table handouts + Excel templates | Solstice graded packet (year 1: Canvas) |
| Discussion sites (after case day) | Anything with student data |

Repo history is forever — solutions must never be committed, even in a "private" folder.

## Structure

- `schedule.yml` — single source of truth for schedule and materials pages
- `materials/` — public PDFs and handouts
- `discussion-sites/` — interactive discussion sites (drop in from Opus builds)
- `files/` — syllabus PDF, verification log template, etc.

## License

Course materials © John M. Barrios. All rights reserved.
