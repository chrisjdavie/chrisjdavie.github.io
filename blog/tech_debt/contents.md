# Unexpectedly poor dev experience after fixing technical debt

## Setting the scene

- I joined a team working on an internal system (other systems triggered it, and a few days later called back to pick up the results)
- 2 other developers, 15 years of code
- the company was expanding, that library (and team) was a consistent bottle neck
- 2 major issues
  - new features taking a really long time to get into the code
  - high turnover in team members - people never stayed in the team more than a year
    - big part of that was it was demoralising to work on the code base
- after a few weeks, turns out we were spending around 10% of our time actually doing development, the rest fighting technical debt
- biggest chunk of tech debt, about 50% of our time, battling with the code base (figuring out where integrations should go, finding the multiple daily crashes, pushing in a fix, picking it up again)
- fixed one chunk of it as a demo, projected it would take 3 months of all 3 of use working on it, but as if was 50% of the time, the work would pay for itself in ~6 months
  - also hoped for less concrete benefits - devs would get to spend that time building out new features, not fighting tech debt
- took a while, but got agreement from various stakeholders to start addressing this
- added end-to-end tests, bought in an open source framework designed for that sort of library, bought in branching, CI/CD, code review, depulicating code, consistent naming, lots of good things

## Results

- It worked - we fixed the tech debt in the library
- Features were released on a much more regular basis, devs were much more productive
- Happy for a few weeks
- instead of spending nearly all our time fighting with the code base, we were spending all our time fighting with the servers the code was running on
  - picking them up, looking for what had caused the code to crash, patching over that, picking it up
- unfortunately, as the business was now getting feature updates on a schedule that worked for them, the team was no longer a bottle neck, the commercial case for tackling it wasn't there (it would have taken another couple of months to deal with all this, based on fixing one of the servers and doing a PoC)
- for the longest time, this was really strange to me. We had been spending all our time fighting the code base, we had fixed it, we weren't fighting it anymore. But where had all that time gone? Why were we now mostly fighting servers, even though the business expectations of the transformation were me?

## Why the dev experience remained shocking

- what's a good dev experience, in terms of tech debt
  - less that 20% of your work time managing debt?
  - perhaps a high target, but have seen it on some projects I've worked on
- main issue was inexperience
- we were naively expecting all the time we spent working on the code tech debt to turn into time working on new features
- the graph below is a visual representation of this - new feature work entirely replacing old tech debt work

![Graph showing tech debt replaced entirely with feature work, with over half of the devs time spent on feature work](expected.svg)

- (of course the actual values are representative - each ticket is different)

- what I think actually happened was that each piece of work took half the time. Exactly what the business needed. But in terms of work spent on each feature, it just removed most of the work on code debt - the amount of time spent on each other part remained the same. So what was experienced was now, the majority of time for each feature was now spent dealing with the other sources of technical debt.

- The graph below shows what really happened - each chunk of work expanding proportionally to fill the space left by the removed tech debt.

![Graph showing all areas of work expanding to replace the removed tech debt, with only 8% extra time being spent on feature work, from a base of 10%](actual.svg)

- So we did have a large increase in the amount of time working on new features - almost double in this example, 10% to 18%. Which is of course better. But as developers, we really didn't notice it. All we noticed was we were fighting other problems, rather than code.

- So what were the other problems?
   - the servers was the problem!
   - had our own in house server farm
   - never updated
   - running different versions of software
   - a couple of the servers had flakey hardware and would crash
   - people would log onto the servers and run things on the fly, in addition to the distributed compute system, crashing things, causing unexpected changes

- Based on what we learnt above, what would happen if we fixed the severs, dealing with 90% of the worst failures?

![Graph showing all areas of work expanding to replace the removed server debt](server.svg)

- We weren't allowed to fix the servers, we did mitigate the worst failures in software - but it would have consumed

## Case for fixing it

the graph here
- 1st graph
- - increasing capacity, recovery from failures
- 2nd graph
- - causes of failures (software, server software, hardware, other)
- obvious thing, rewrite the code that ran the processing
- expected outcome graph (all software failure to clean)

## Case against fixing it

- - they're rightly scared of change (every change seriously damaged the system, so they made it as infrequent)
- - - distrust in the system
- - - distrust in the competence of the devs
- - - proprosing a rebuild when even the smallest change would often knock the system down for days

- our team was different - we'd set up a dev system, lots of manual testing, and our changes rarely broke things (did sometimes, but other teams changes did all the time, so ours weren't noticed, and ours were quick to fix as we'd put in additional, basic logging)

- eventually, the complaints of the devs and customers were heard, and we were assigned to fix it

## Fixing it
- after a few months of this being a largely intractible problem, devs were finally listened to, and we were allowed to tackle the problem
- adopted external libraries and frameworks, set up automated testing, CI/CI, regression testing, began the gradual rebuild (working through fixing things, keeping compatibility between the old and new, so always worked). 
- 3 months of work later, and it was transformed. 
- - All of the software was fixed, 
- - Mostly clear, well understood by team
- - Straightforward to add new features (work that would have taken weeks took hours)
- - robust logging, restart points and automatic recovery
- - Quickly diagnose failures
- - if it passed the integration tests, 90% of the time worked in prod (previously, deploys never worked)
- - 95% of new code into processing system, if it passed the quick tests it passed the full integration tests
- - It was great
- part of it worked
- increase in dev capability
- deploys went from being never sucessful and slow to fix to being nearly always sucessful and quick to fix
- But what I expected hadn't happened, we didn't move to some productive nivana where we were spending most of our time building out features
- proprotional growth
- but, it did allow us, a team of 3, to increase data through put to 50x the initial level (libraries were 20% faster, was mainly through not having to pick up broken things as much)
- satisfied one customer
- sales bought in 2 or 3 more customers
- pressure on the system went up, failures went up
- this time, needed to fix the servers next

## It didn't work

```
Make this story happier - I came up with a proposed solution, my contract was up, and the role had moved on from what I was looking to do - it had transformed from being a software dev role to being a server picker-uper, and was a small company, wasn't really much else for me to do. And also, I was very good at picking up the servers and very familiar with the software after the rewrite, so the company wasn't keen to have me work on anything else.
```
- new graph

- this conversation went on for several months, back and forth between the people who worked on the servers (who all wanted them to be fixed) and commercial and the managers, who just wanted to scale up throughput
- 2 obvious solutions
- - fix the servers
- - - new hds in all the servers
- - - central management of OSes and minimal software for running system
- - - deploy code in containers (poc worked), software, keep all the servers on the same versions of the software
- - - keep it all consistent
- - - (obviously suboptimal, we were a data processing company, not a server farm company)
- - managed servers, cloud servers
- - - deploy the containerised software  
- the tech managers weren't interested
- their solution was to recruit more people to pick up the system, buy more servers to process more things
- seemed the complexity of the problem would not scale linearly - you add 10 people and 40 servers, all pulling through the workload, likely complexity of the system would require more than just 10
- unsure what happened - after 4 months of conversations around this subject, I was offered another role, and obviously took it :)

## Moral of the story

- large moral, is if you get in a situation were you're fixing technical debt, the fixes won't free up the amount of time you're expecting them to do. If you're aiming to increase dev resources, it worked. If you're aiming to make you devs happier, it won't
- the other is to do with the challenge of change
- - it takes a lot of work to persuade some people that things should change
- - they're rightly scared of change (every change seriously damaged the system, so they made it as infrequent), and slow to trust
- - is very difficult without high up support (still small company, but really the managers didn't really want things to change)
- - without a language to talk about change, the experience and skills to make change safe, and with a willingness to develop trust, change is a super hard thing to do
- - even when change is introduced, it's slow, painful, and when major problems are fixed, it'll likely uncover other problems that the pain from the first one was covering up
- the importance of CI/CD, small changes, robust integration testing, robust unit testing, fixing issues when they're small so they don't become large (and thus hiding other issues)
