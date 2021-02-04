My personal website. If you want to render it, the easiest way is to run the command

 `inv render`

This runs the `render` function in the `tasks.py` file.

This requires `Python3.8` , `invoke` and probably `virtualenv` all installed. I'm pretty sure you can install `invoke` and `virtualenv` via `pip` . It might be `bash` specific too (tested on `Ubuntu 20.10` )

This renders the templates in the `templates` directory, using the data in `testimonials.json` and the jsons in `portfolio/<page_name>/data.json` . Once it's rendered, it dumps a bunch of `html` files around - `portfolio.html` in the root here and the portfolio pages in `portfolio/*` .

This code isn't my best, and the JavaScript is pretty awful - but it's nearly the only JS I've ever written. 

## Portfolio page structure

These are rendered using `templates/portfolio_page.html.jinja` . The data for each portfolio page is held in the page directory, `portfolio/<page_name>/data.json` . The text is in `portfolio/<page_name>/contents.md` - these markdown files also contain html and javascript. The images referred to in `contents.md` are in this same folder, as is the javascript that generates graphs.

## Blog pages

There is `blog/` folder, structured in the same way as portfolio pages. These are part of an idea I have to blog and tweet regularly, but it's not my current focus. If I decide to do it in earnest, I'll finish the pages there and pick that all up, but it's fairly far down the list for now.

# Comments on using Python and Jinja

I've built this page using Python and jinja2, generating html pages. These html pages use javascript packages (directly bootstrap and chartjs) and a small amount of custom javascript to generate interactive and reactive content.

I'm sure there's a nicer javascript way of writing this build the page dynamically, but I'm a data engineer/backend dev and this is a pretty straightforwards way of me setting up this while mainly only having to learn a templating language (beyond what I already knew about css and bootstrap).

I've learn a bit of javascript doing this, largely for plotting the interactive plots. The javascript is not great, but the graphs are pretty.
