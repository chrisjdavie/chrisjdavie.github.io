# Climatic patterns in the algorithm

## <small> Climatic patterns in the project </small>

___

Applying climatic patterns from chapter 3 to lul

* small project, patterns are there, but perhaps don't matter so much
* * but they are there
* * and it they're there
* * and if they're there in such a tiny example, they're there in much larger projects
# Patterns observed

## No single method fits all

* R&D methods in the R&D phase
* switching out to more formalised dev methods as it evolves
* incorporating more systematic, productionised, processes as time went on change
* change was more time consuming, but a hell of a lot safer - a requirement, as Blake got used to things working better, going backwards wasn't an option, similarly with customers - it worked and needed to stay working, even if, at the start, it worked much less well

## Components can co-evolve

* There is a risk, in telling these stories, that it makes it sound deliberate
* This evolution was not deliberate - I was merely solving the problem in front of me, following well-trod paths
* While I was deliberate in building (*not* evolving) the solver, everything around that - the config, the tests, the test suite, the dockerisation, the configuration interface, the knowledge of the surrounding problems, all were built and developed in reaction to problems

## No choice over evolution (Red Queen)

* even in this setting, it was not possible for the solver and components to *not* evolve, as I was solving a problem for a customer
* the components I was only working on to support the solver naturally evolved too

## Efficiency does not mean a reduced spend

* features didn't really speed up, in spite of additional knowledge and existing code base - the time associated with including new things while keeping the old things behaving kinda balanced this out
# Evolution to higher order systems results in increasing local order and energy consumption
* Not sure what "local order" means here
* Def increase in energy consumption - parallel by default algorithm, extra time handling corner cases, compute time in running through the hundreds of cases in the test cases

## Efficiency enables innovation

* Not so much providing that as the innovator; work enabled by other's research, Python, Cython, pytest, parallel programming design patters, Docker, json, git, restful design patterns, processes (TDD)
* really the ecosystem relied on to be fuctional and stable is kinda huge for a fairly simple, one man project

## The less evolved something is then the more uncertain it becomes

* Before starting, no idea of the correct approach, only of incorrect ones
* R&D of the initial algorithm - many different routes to the end result
* Settled on a choice of algorithm
* Repeated again and again, solving a sub-problem, unsure of correct approach, research, selected, narrowed down
* Results, sucess, solving problem became more predictable as things evolved more
