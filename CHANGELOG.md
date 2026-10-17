# Changelog

## Unreleased

- Post pages: the author card now comes right after the tags, followed by previous/next post links (with thumbnails; previous = older, next = newer) and then the related posts. New labels `prevPost` and `nextPost`.
- Categories page (`categories.qmd`, created by the hook like `tags.qmd`): a category cloud and a paginated post list, linked as `categories.html#category=<name>`.
- Related posts show each post's thumbnail (its front-matter `image`) beside the title and date (`img/placeholder.svg` when a post has none; the thumbnail is dropped if it cannot load). The hook now writes `image` into `blogkit-data.js`.
- The sample site's navbar gets a Categories link and it has a `page-footer` example (the extension already styles `.nav-footer` in both themes).
- `publish.sh` re-renders `index.qmd` after single-post renders: Quarto's listing refresh renders the homepage without the extension's format (light theme only, no CSS or scripts). If you render posts by hand, run `quarto render index.qmd` afterwards, or do a full `quarto render`.
- Small-screen "On this page" menu works when Quarto rewrites TOC links to absolute URLs.
- Tag cloud in the sidebar is taller (18rem) before it scrolls.
- Inline code and plain (language-less) output blocks are styled separately, in both themes.

## 0.1.0

First release, extracted from a working Quarto blog.

- `blogkit-html` format: dark/light theme with navbar toggle, styles, code-reveal buttons.
- Pre-render hook `build_site_data.py`: writes `blogkit-data.js`, copies `blogkit.js`, generates author pages and `tags.qmd`.
- Browser script: sidebar archive and tag cloud, post tags, related posts, author cards and links, tags page, author pages with filters and pagination, small-screen table of contents.
- `publish.sh`: render, commit, push.
- Sample site with six posts by two authors, usable as a `quarto use template` starter.
