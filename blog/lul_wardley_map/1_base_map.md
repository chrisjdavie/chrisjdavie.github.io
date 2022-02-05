# Lineup Lab described with Wardley Maps

## <small> Learning about Wardley Maps, using them to describe developing an algorithm

___

Wardely Maps are a technique to enable communication of the structure and direction a project, to allow better decisions with this projects. As a developer, they have the potential to allow me to communicate many complexities of the decisions I'm making on technical projects to my business colleagues - more clearly represent my understanding of the environment (organisational structure, teams around), communicate how the things I'm building depend on each other and this wider environment, and reach better informed decisions with my colleagues have, day-to-day, exposure to the detail of different chunks of the problem.

As I'm learning Wardely Maps, I'm using them to describe the evolution of a project I worked on for a year, and it's evolution from R&D to a core compentent driving revenue at a startup.

# Lineup Lab

Lineup Lab helps sports gamblers make better decisions, with the aim of enabling them to win more; I've written more about it **HERE**. My algorithm provided the advice; given a set of sports people, some statistics around their projected performance, and details of the game set up, my algorithm provided the optimal configuration of sports people to bet on.

## A graph of my project

My algorithm started out as an R&D project, researching and testing different approaches and adaptions that would allow this problem to be solved. The project gradually progressed to becoming more fully fledged, broader - feature expansions; different sports, optional rules, different solution techniques. I almost included more sophisticated development processes - automated testing, test driven development, refining the API, and more systematic delivery of the software to my customer. Additionally I used more sophiticated software techniques - multiprocessing, design patterns, internal abstractions of the interface.

This was a fascinating project to learn from, and quite rare - it's unusual to be able to prototype an algorithm, and grow it into a fully fledged project.

**The paragraph below is the core, move it up or something**

But while I can list the techniques I used above, and can discuss why I made the changes I did, the model for the system mainly exists in my mind (and also in code, but no-one else has read it in detail). This required a high degree of trust between me and my client around decisions being made. It worked really well, but when I first read about Wardley Maps, I realised this was framework that could very easily communicate many much of the important high-level decisions I was making, without needing to communicate so much detail that it becomes unwieldy.

* Move knapsack problem to low product - knowledge, "Theory"
# What is a Wardley map

Here, I'm using a Wardley Map as a tool for communicating the evolution of this algorithm. There are many more layers to mapping, helping strategic decision making for entire organisations, but it's really interesting at this granular level too (I'm working on a much larger, inter-organisation map for a large research project - big and small!)

* X axis - evolution
* * In this context, software
* Y axis - visibility
* * Distance to customer, direction of dependencies
* What are the lines?
* * Links in a dependency chain (the dependencies are not universally downwards, away from the customer)
* *  "There is a flow of risk, information and money between components."
# Explain the project by expanding nodes
* from the first, customer facing nodes, representing the solution to customer problems
* adding on the next layer, next layer, etc, until external contract
# Initial R&D project
* R&D from blake
* Brief 
* * Based on provided example, build solver
* * 2/3 liner on LuL, link to longer write up
* MAP!
* And I ran with it
* * Blake provided example
* * wrote direct solver
* * looked up research
* * implemented a solver
* * ran against the prototype
* Explain arrows
* * Blake gaining more experience
* * As project ran, Blake got more examples
* * The main point of the project was to drive the prototype to "custom built" - something that could be used in production to drive customer value
# First working solver
* describe stage ADD MOAR
* extra nodes - built interface
* nodes changed nodes - direct solver became part of the manual tests
* switch names - Prototype to solver
* Dependency isn't so much on research, it's now on my knowledge
* Explain arrows
* * Focus of the work was the solver, but the other processes went along with it
# More sports
* Bugs also drove the examples
