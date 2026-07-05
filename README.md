# MGT 816 Fall 2026 — Course Website

Course hub for **The Private Firm CFO: Accounting and Finance Strategies** (Yale SOM, Fall-1 2026).

**Live site (once public):** https://barrios88.github.io/mgt816-private-firm-cfo/

> **Currently private / not deployed.** Repo stays private while the course is being built; the Pages workflow is disabled. To go live: make the repo public → Settings → Pages → source "GitHub Actions" → re-enable the `Publish Quarto Site` workflow → run it once.

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

## Dropbox + git coexistence (this working copy lives in Dropbox)

The canonical working copy sits inside Dropbox; GitHub is the sole carrier of git history. Three rules keep them from fighting:

1. **Dropbox never syncs git or build state.** `.git/`, `.venv/`, `_site/`, `_freeze/`, and `.quarto/` are marked with the `com.dropbox.ignored` xattr (they show a gray minus badge in Finder). If one of these directories is ever recreated (fresh clone, `venv --clear`, first render), re-mark it:
   ```bash
   xattr -w com.dropbox.ignored 1 .git .venv _site _freeze .quarto
   ```
2. **Source files stay downloaded.** Keep this folder "Available Offline" in Dropbox (right-click in Finder). Online-only eviction turns files into 0-byte stubs, which git would see as emptied files.
3. **Stub commits are blocked.** A local pre-commit hook (`.git/hooks/pre-commit` — not versioned, recreate on new clones) refuses to commit any staged file carrying the `com.dropbox.placeholder` xattr. If it fires, materialize the file (`open -g -a TextEdit <file>`) and retry.

On any other machine, `git clone` from GitHub — do **not** re-init git inside the Dropbox copy there (Dropbox doesn't carry `.git`, by design).

## License

Course materials © John M. Barrios. All rights reserved.
