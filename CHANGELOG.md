# Changelog

## Unreleased

- Post pages (desktop): the archive and tag cloud sit directly below "On this page" and follow its length, instead of being pushed to the bottom of the sidebar; the TOC is no longer sticky.
- Sidebar tag cloud shows only the 15 most-used tags (no scroller), followed by an "All tags ›" link to the tags page.
- Hero stats strip has an icon (inline SVG, no dependency) before each item: posts, topics, last update and RSS.
- Light theme: generated figures (post-body SVGs, and PNG covers that have a same-named SVG, flagged `adapt` in `blogkit-data.js`) are inverted in the light theme so they no longer show as dark boxes; photos and real plots are left alone. White hero search field in light mode.
- Hero tools are now rendered into the page at build time: the hook writes `_bk-hero-tools.html` (search, chips, stats) and you add `{{< include _bk-hero-tools.html >}}` in the hero instead of an empty `<div id="bk-hero-tools">`. The tools are present from the first paint (no pop-in); `blogkit.js` only attaches the search. New option `hero-tagline`. The old empty-div form still works (built in the browser).
- Smoother homepage load: the hero tools reserve their height until the script fills them (the page below no longer jumps), fade in, and the listing's own filter box is hidden by CSS from the start instead of flashing.
- Hero tools are more compact: search and a single row of chips (default 5, scrolls sideways, plus a "more" link to the tags page) sit side by side from 768px up; `data-tagline="..."` on `#bk-hero-tools` puts a one-line description above the stats line (hidden on phones). New label `moreTopics`; `hero-topics` now defaults to 5.
- Homepage hero tools: add `<div id="bk-hero-tools"></div>` inside a hero and `blogkit.js` fills it with a search box (drives the listing's filter, so keep `filter-ui: true`), chips for the most-used tags and a stats strip (posts, topics, last update, RSS). Labels `searchPosts`, `topics`, `updated`, `rss`; option `hero-topics` (number of chips).
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
