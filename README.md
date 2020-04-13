My personal website. If you want to render it, the easiest way is
to run the command

`inv render`

This requires `Python3.8`, `invoke` and probably `virtualenv` all installed. I'm pretty sure you can install `invoke` and `virtualenv` via `pip`.

This renders the templates in the `templates` directory, using the data in `testimonials.json` and the jsons in `portfolio/data`. Once it's rendered, it dumps a bunch of `html` files around - `index.html` in the root here and the portfolio pages in `portfolio`.

I'm sure there's a nicer javascript way of writing this to open up the jsons and put them in page dynamically, but I'm a backend dev and this is a pretty straightforwards way of me setting up this while only having to learn a templating language (beyond what I already knew about css and bootstrap).
