# Changelog

## Unreleased

- Tags and categories pages list all posts (paginated) until a tag or category is picked, instead of showing only a hint. New label `allPosts`.
- Tag, category and author pages list posts as thumbnail rows (cover image, title, date and description), the same look as related posts.
- Desktop: the "On this page" table of contents is sticky, so it stays in view while the article scrolls. It sits in a track above the archive and tag cloud and stops before them, so nothing overlaps and the sidebar has no inner scrollbar.
- Post pages: the author card now comes right after the tags, followed by previous/next post links (with thumbnails; previous = older, next = newer) and then the related posts. New labels `prevPost` and `nextPost`.
- Categories page (`categories.qmd`, created by the hook like `tags.qmd`): a category cloud and a paginated post list, linked as `categories.html#category=<name>`.
- Related posts show each post's thumbnail (its front-matter `image`) beside the title and date (`img/placeholder.svg` when a post has none; the thumbnail is dropped if it cannot load). The hook now writes `image` into `blogkit-data.js`.
- The sample site's navbar gets a Categories link and it has a `page-footer` example (the extension already styles `.nav-footer` in both themes).
- `repair_index.py` post-render hook (add `post-render: _extensions/blogkit/repair_index.py` under `project:`): rendering a single post makes Quarto refresh the homepage listing without the extension's format (light theme only, no CSS or scripts); the hook re-renders `index.qmd` afterwards. Replaces the extra step previously added to `publish.sh`.
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
