# Native Jekyll rewrite of plano333.pt

## Why

The site is a mirror of WordPress output: each page is about 200 KB of Elementor markup, with 96 KB of inline theme CSS. Editing a sentence means searching through generated HTML. The goal is a site that is easy to edit, with every page in Markdown and the repeated parts shared, while keeping the current look.

## Goals

- Every page is one `.md` file: front matter plus Markdown text, with include tags for special blocks.
- Repeated parts are reusable components in `_includes/`.
- One small hand-written stylesheet carries only the styles the pages use.
- The look matches the current site: colours, fonts, spacing, layout, and mobile behaviour.
- GitHub Pages keeps rebuilding the site on every push to `main`, using the existing workflow.

## Non-goals

- No blog. Everything is a page, and there is no `_posts` folder or post layout.
- No WordPress features: feeds, `wp-json`, comments, search.

## Anti-goals

- A visible change in look. Old and new screenshots of each page must match closely.
- Lost text. Every page keeps its visible text, word for word.
- Leftover WordPress, Elementor, Astra or Complianz CSS/JS in the repo.

## Approaches

1. **Keep the WordPress CSS, wrap the markup in components.** The look is identical with no effort, but the markup stays verbose and tied to Elementor's classes. Rejected by the owner.
2. **Clean rewrite with the same look (chosen).** Simple semantic HTML and one small stylesheet that reproduces the look. The CSS gets rebuilt by hand and checked against screenshots.

## Design

- **Layouts.** `_layouts/default.html` holds the `<head>`, header, footer and consent banner. `_layouts/page.html` adds the dark title banner (background image from front matter) above the content.
- **Navigation.** `_data/navigation.yml` holds the menu, footer link columns and social links. The header and footer both read it.
- **Components** in `_includes/`:
  - header with a CSS-only mobile menu, and the footer
  - title banner
  - CTA pair: the yellow "Conheça o Plano 3-3-3" and dark "Participe no Treino" banners
  - button
  - icon card
  - image card
  - image
  - YouTube video (thumbnail that loads YouTube only on click)
  - FAQ accordion (native `<details>`, no JS)
  - icon list
  - divider
  - social icons
  - map embed
  - section wrapper with background variants
- **CSS.** `assets/css/main.css`, using CSS custom properties for the colours and fonts from the Elementor kit (`--e-global-color-*`). Fonts are Manrope and Plus Jakarta Sans from Google Fonts. Mobile breakpoint is 921 px, which is Astra's.
- **Icons.** Font Awesome is replaced with inline SVGs for only the icons used.
- **Assets.** Images move to `assets/images/`. Only files the pages reference stay; `wp-content/` and `wp-includes/` are deleted.
- **Analytics and consent (owner's choice).** Google Analytics `G-PV5EZG98FS` loads only after the visitor accepts in a small consent banner. The choice is stored in `localStorage`. About 20 lines of JS, no library. The YouTube component also loads nothing from YouTube until clicked.
- **URLs.** Every page keeps its current path (`/faq/`, `/historia/`, and so on) via `permalink` in front matter.

## Verification

- A text check compares each new page's visible text with the mirrored original.
- A link check confirms every internal link and asset resolves in `_site/`.
- Side-by-side screenshots of old and new versions, desktop and mobile, for each page.

## Left to the builder

- Exact component parameters and markup.
- How to group CSS rules within the one file.
- Which images to resize, if any are much larger than displayed.
