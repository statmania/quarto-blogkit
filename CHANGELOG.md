# Changelog

## 0.1.0

First release, extracted from a working Quarto blog.

- `blogkit-html` format: dark/light theme with navbar toggle, styles, code-reveal buttons.
- Pre-render hook `build_site_data.py`: writes `blogkit-data.js`, copies `blogkit.js`, generates author pages and `tags.qmd`.
- Browser script: sidebar archive and tag cloud, post tags, related posts, author cards and links, tags page, author pages with filters and pagination, small-screen table of contents.
- `publish.sh`: render, commit, push.
- Sample site with six posts by two authors, usable as a `quarto use template` starter.
