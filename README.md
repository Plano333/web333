# web333

The [plano333.pt](https://plano333.pt) website, built with Jekyll. Every push to `main` rebuilds it and publishes it to GitHub Pages at <https://plano333.github.io/web333/>.

## Links and paths

GitHub serves the site from the `/web333/` subfolder, so every local path needs that prefix. Write paths from the site root, starting with `/`, and let Jekyll add the prefix.

Include parameters such as `url=` and `src=`, and the links in `_data/*.yml`, need nothing extra because the includes add the prefix. In page text, wrap the path in `relative_url`, for example `[FAQ]({{ '/faq/' | relative_url }})` or `<img src="{{ '/assets/images/x.webp' | relative_url }}">`.

`check_site.py` fails the build if a local path is missing the prefix.

### Moving to the custom domain

When the DNS record for `teste.plano333.pt` (a CNAME pointing to `plano333.github.io`) is in place:

1. In `_config.yml`, set `url: https://teste.plano333.pt` and `baseurl: ""`.
2. Set the custom domain in the repository's Pages settings.

Page paths stay as they are.

## Editing a page

Each page is one Markdown file in `_pages/`, such as `_pages/faq.md` or `_pages/historia.md`. The front matter sets the URL (`permalink`), the title, the banner image and the promo cards at the bottom. Below it is the page text in Markdown, with `{% include %}` tags for the special blocks.

The folder doesn't appear in URLs, so every new page needs its own `permalink`.

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
| `social.html` | Facebook and YouTube icons |
| `icon.html` | Inline SVG icon by name |
| `banner.html`, `cta.html`, `header.html`, `footer.html`, `consent.html` | Used by the layouts |

`_includes/faq.html` holds the questions shared by the home and FAQ pages. It uses native `<details>` and `<summary>` elements, so the accordion needs no JavaScript.

Google Analytics loads only after a visitor clicks "Aceitar" in the cookie banner.

## Previewing locally

```sh
gem install jekyll -v '~> 3.10' webrick
jekyll serve
```

Then open <http://127.0.0.1:4000/web333/>.

## Checking a build

```sh
jekyll build
python3 check_site.py
```

The check verifies all 14 pages, shared landmarks, local links, image and stylesheet assets, and rendered Liquid. GitHub Actions runs it before deployment. Python 3 is the only requirement beyond Jekyll.
