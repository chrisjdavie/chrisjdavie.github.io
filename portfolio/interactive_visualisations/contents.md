<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.0.0-beta.9/chart.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/patternomaly/1.3.2/patternomaly.js"></script>
<script src="../blog/fix_code_base_not_dev_exp/bar_chart.js"></script>
<script src="sports_algorithm/beta_annotations/chartjs-plugin-annotation.min.js"></script>
<script src="../portfolio/sports_algorithm/scatter_chart.js"></script>

# Interactive data visualisations

## <small>Data visualisations using browser technologies</small>

___

Building interactive data visualisations, to learn JavaScript and prettier ways of displaying data.

<canvas id="demo_bars" class="plot"></canvas>
<script>draw_chart("demo_bars", 'After', [10, 40], [20, 30], [30, 20], [40, 10])</script>

*A bar chart visualisation, for a blog post I might finish*

This portfolio site had many graphs, largely static images built in Python. Python produces crisp academic graphs, but not interactive, web-based visualisations.

I'd like to build dynamic visualisations, but Python's are ugly, with odd dynamic behaviour. It seems sensible to use JavaScript, it's the language of the web, and learning it will let me build more things!

So I researched JavaScript data visualisation libraries - there are a lot! I chose Chart.js - a well documented, easy to use, feature rich, well maintained and widely used library. I'm pleased with the visualisations I then built, above and below, judge for yourself.

<canvas id="scatter_chart"></canvas>
<script>manage_chart_dynamics()</script>
*A visualisation of a tree, the type of algorithm developed for *Lineup Lab*.*

There are great features in Chart.js - simple to use, easy to customise, large plugin ecosystem; I really like annotations for drawing on graphs, and patternomaly, making bar charts colour-blind friendly. There are difficulties - it's hard to control precisely - the legend for the lines is a box, and there are too many lines on the axes, reducing them takes much code.

I found customisation in Python to be more straightforward - part of that is familiarity.

Learning JavaScript went well - functions, callbacks, objects, browser console use. I integrated this into my portfolio pages, using resizing and JavaScript files. I also learnt what jQuery is, but didn't use it.

It highlighted how unfamiliar I am with JavaScript - my code is ugly! I also have no idea how to test visualisations, test-first development for this would be interesting.

This has gone really well - interactive visualisations, a decent introduction to JavaScript, and an enjoyable project!
