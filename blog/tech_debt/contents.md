# Failing to improve dev's experience when fixing technical debt

WRITE SUMMARY

## Setting the scene

I joined a team working on an internal service. This service was a consistent bottle neck; new features took a really long time to develop, and developers didn't stay in the team beyond a year.

It turned out we spent 10% of our time developing new features, the rest fighting technical debt. The biggest single chunk, about 50% of our time, was battling with the code base; figuring out what code did what, where new code should go, fixing the multiple daily crashes, manually resuming the jobs - we couldn't restart them, as nearly all runs failed.

We fixed one chunk of the code as a proof of concept, and projected the full fix would take 3 months for the team and free up half our time.

The commercial case was clear - faster feature development, the work paying for itself in 6 months - and then more dev time, doing more rewarding work.

After a couple of months, we started our rebuild; first adding automated testing, bought in an appropriate framework, git, gitflow, CI/CD, consistent naming and code review. We deleted, rewrote, refactored and depulicated code, increased the test coverage and added automatic resume points, mitigating the damage from crashes.

And slightly under the projected 3 months, we were done.

## Results

It worked - we had fixed the tech debt in the code. Features were released more rapidly, on a more predictable caidence and the system was reliable. It was also 20% faster, a free benefit. Everyone outside the team was pleased.

And the team was at first happy, more focused and productive. But this faded - we were now spending all our time fighting with the servers; looking for what had caused the crashes, mitigating that, relaunching the run.

This was really strange - we had been spending all our time fighting the code base, and had fixed it. But where had all that time gone? Why were we now mostly fighting servers, even though our productivity was boosted?

## Why the dev experience remained shocking

We were naively expecting all the time we spent working on the code tech debt to turn into time working on new features. I've visualised this expectation below, new work entirely replacing code debt work.

![Graph showing tech debt replaced entirely with feature work, with over half of the devs time spent on feature work](expected.svg)

The values in the plot is representative - each task is different.

The time spent on code debt was reduced, the time spent in all other tasks remained the same. So the majority of time for each feature was now spent dealing with the other sources of technical debt.

The graph below represents the work our team was doing, in terms of total time spent working on each type of task - each other area of work expanded to fill the space left by the removed tech debt.

![Graph showing all areas of work expanding to replace the removed tech debt, with only 8% extra time being spent on feature work, from a base of 10%](actual.svg)

We did have a large increase in the amount of time working on new features - almost double in this example, 10% to 18%. An improvement, but a small minority - really didn't notice the improvement. We noticed fighting other problems, rather than code.

The next biggest problem was our company server farm! There were a host of issues; the software was rarely updated, most servers each running different versions of packages (in one case, an entirely different OS). It used a dated, unsupported distributed compute platform. Two of the servers had flakey hardware and would crash. People would log onto the servers and run things on the fly, crashing things and causing unexpected changes

So what would we spend our time on, if we fixed the severs, dealing with 90% of the worst failures?

![Graph showing all areas of work expanding to replace the removed server debt](server.svg)

Approaching half of our dev time would then be doing new work. This should be noticable, but it still much still less than you'd aim for. To get so something reasonable, say 80% of time developing, we'd have to significantly reduce the remaining code debt, probably tackle the servers a second time and figure out the other sources of problems - which included external dependencies not working well.

## We didn't get to fix it

In the end, we didn't get to fix these problems. The team was no longer a bottle neck, the commercial case wasn't there - it would have taken around another couple of months to fix the servers, let alone solving the other problems.

These were also shared problems, the servers and the external dependencies, we'd need to fix these problems with other teams, who didn't necessarily even agree they were problems that needed fixing!

If it was merely solving the technical problems, perhaps if our team dedicated 6 months to a year to resolving the issues we could fix it, but that's a lot to ask from a company. 

We successfully fixed the tech debt as bottle neck in the company, but it wasn't enough to improve the experience of working on the system - the team members kept moving on at the same rate!

## Main takeaways

That I was extremly naive and unrealistically optimistic about fixing tech debt. If the hope is to improve the experience of developers; more engaged, building and learning rapidly and generally happier and more hopeful, tackling technical debt is likely going to take a very long time, even after the commercial benefits are very clear - happy commercial stakeholders, and unhappy technies.

It also taught me to be focused on the quality of code and systems I'm working on. It is really, really important address repeated pain points early. Recovery from poor quality systems will take more time than people are likely willing to spend, it's much more straight forward to figure out how to not get into that state in the first place.
