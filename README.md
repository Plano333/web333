# web333

Static copy of [plano333.pt](https://plano333.pt). WordPress rendered these pages, and Jekyll now builds them as plain HTML.

Each push to `main` rebuilds the site and publishes it to GitHub Pages at <https://teste.plano333.pt>.

## Editing

Every page is a folder holding the HTML that WordPress generated, for example `faq/index.html` and `historia/index.html`. Edit those files directly. They're long and machine-written, so search for the text you want to change rather than reading from the top.

Images, CSS and JavaScript sit under `wp-content/` and `wp-includes/`, at the same paths the old site used.

## Previewing locally

```sh
gem install jekyll -v '~> 3.10' webrick
jekyll serve
```

Then open <http://127.0.0.1:4000>.
