# web333

The [plano333.pt](https://plano333.pt) website, built with Jekyll. Every push to `main` rebuilds it and publishes it to GitHub Pages at <https://teste.plano333.pt>.

## Editing a page

Each page is one Markdown file at the repo root, such as `faq.md` or `historia.md`. The front matter sets the title, the banner image and the promo cards at the bottom. Below it is the page text in Markdown, with `{% include %}` tags for the special blocks.

Shared parts live in one place each:

- `_data/site.yml`: header menu, footer links and social links.
- `_data/cta.yml`: the yellow and navy promo cards. A page picks two of them with `cta: [plano, treino]`.
- `_includes/`: the components. Each file has a comment at the top listing its parameters.
- `assets/css/main.css`: the only stylesheet.
- `assets/images/` and `assets/files/`: images and PDFs.

## Components

| Include | What it is |
|---|---|
| `button.html` | Link button: `primary`, `navy`, `navy-white` or `outline` |
| `icon-box.html` | Card with icon, title and text |
| `image-box.html` | Card with image, title and text |
| `image.html` | Image, optionally linked |
| `youtube.html` | YouTube video that loads only when clicked |
| `divider.html` | Line, optionally with a date in the middle |
| `map.html` | Embedded map |
| `social.html` | Facebook and YouTube icons |
| `icon.html` | Inline SVG icon by name |
| `banner.html`, `cta.html`, `header.html`, `footer.html`, `consent.html` | Used by the layouts |

The FAQ accordion needs no include. It is plain `<details>` and `<summary>` inside `<div class="accordion">`.

Google Analytics loads only after a visitor clicks "Aceitar" in the cookie banner.

## Previewing locally

```sh
gem install jekyll -v '~> 3.10' webrick
jekyll serve
```

Then open <http://127.0.0.1:4000>.
