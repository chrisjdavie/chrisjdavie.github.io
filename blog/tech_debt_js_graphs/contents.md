<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/patternomaly/1.3.2/patternomaly.js"></script>
<script src="tech_debt_js_graphs/bar_chart.js"></script>

# Fixed code base, not dev experience

## <small>Increased productivity, didn't make us happy</small>

___

We fixed the worst of the code base, but were didn't notice any improvement in our day to day work. Our work was completed in half the time, but 80% of our time was still fighting broken systems. This was not enough to improve the developer experience.

## Improving the technical situation

For my team, new features took a long time and developers didn't stay at the company beyond a year. This was in large part due to spending 90% of our time fighting broken systems. About half was battling the code base; figuring out spaghetti code, where new code should go, fixing daily crashes, manually resuming runs - nearly all runs failed.

We fixed one chunk of code as a proof of concept and projected a full fix would take 3 months and free up half our time. We'd get faster feature development, the work paying for itself in 6 months, and work would be more rewarding. Some politicing later, we were given the green light.

Two months later, we started; first added automated testing, bought in appropriate libraries, git, gitflow, frequent integration and deployments, consistent naming and code review. We deleted, rewrote, refactored and deduplicated code, increased test coverage and added automatic resume points, mitigating the remaining crashes.

In slightly under the projected 3 months, we were done.

## Development time increased, but developers were still unhappy?

It worked - features were released rapidly on a regular schedule and the service was more reliable. The code was also 20% faster, a free benefit. Everyone outside the team was pleased. The team was, at first, more focused and felt more productive. 

But this faded - we were now spending most of our time fighting with the servers; looking for what had caused the crashes, managing that, relaunching the runs. We had fixed the code base, where had that time gone? Why were we now mostly fighting servers, even though our productivity was boosted?

## Man hours for new work stayed the same

We naively expected the time we spent on code problems would be replaced with time on new features. I've visualised this expectation below, new work replacing work on code problems.

<p class=plot-title>Expected time spent on catagories of work, <br>before and after resolving code problems</p>

<canvas id="bar_expected" class="plot"></canvas>
<script>draw_chart("bar_expected", 'After (Expected)', [40, 40], [50, 5], [10, 55])</script>

In reality as the time spent on code problems was reduced, the time on all other tasks remained the same - the majority of time now spent managing the other broken systmes.

The graph below represents the actual proportion of time spent on each type of task before and after the fix - other areas of work expanding to fill the time left by removed code problems.

<p class=plot-title>Actual time spent on catagories of work, <br>before and after resolving code debt</p>
<canvas id="bar_actual" class="plot"></canvas>
<script>draw_chart("bar_actual", 'After (Actual)', [40, 73], [50, 9], [10, 18])</script>

We did have a large increase in the amount of new work - almost double. But still a small minority - we didn't notice the improvement.

The next biggest problem was the company server farm. The severs were rarely updated, each server running different OS and software versions, with different configurations. It used an unsupported distributed compute platform. Two of the servers had flakey hardware and would crash. People would log onto the servers and run code, causing crashes and unexpected changes.

So what would we spend our time on if we fixed 90% of the server problems?

<canvas id="bar_servers" class="plot"></canvas>
<script>draw_chart("bar_servers", 'After (Actual)', [18, 36], [9, 18], [18, 36], [55, 10])</script>

Around a third of our time would then be doing new work, a large increase but still a minority. To get to 80% of our time on new work, a good target, we'd need to reduce the remaining code debt, tackle the servers again and fix other problems - including external dependencies.

## We couldn't fix it

In the end, we didn't fix these problems. The team was no longer a bottleneck, the commercial case wasn't there - it would have taken months to fix the servers. These were also shared, the servers and the external dependencies, and other teams didn't agree these were problems!

To solve these, our team would have to dedicate perhaps a year to them - too much to ask from a company. 

For the company, we successfully fixed the bottleneck, but it wasn't enough to improve the experience of working on the system - team members kept moving on!

## Avoid the situation, the fix may be too hard

Tackling enough technical issues to improve developer experience can take much longer than gaining commercial benefits - happy commercial stakeholders, but unhappy techies.

It's important to focus on quality, addressing pain points early - recovery from poor quality systems will take a long time, perhaps creating tension with commercial stakeholders, in this case too long to be allowed. If you're allowed and able, it's best to avoid this situations entirely!
