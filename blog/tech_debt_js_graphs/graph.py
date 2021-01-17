"""
Draw blog post graphs

This code is pretty hacky - I need it to run well once :)
"""
from dataclasses import dataclass
from typing import List, Tuple

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import patheffects
from matplotlib import patches


def draw_tech_debt_plot(
        data_series, bar_labels, graph_title, debt_names, hatching, colors):

    # reverse the data stratification, top to bottom
    data_series = [dat[::-1] for dat in data_series]

    debt_names = debt_names[::-1]
    hatching = hatching[::-1]
    colors = colors[::-1]

    # setup figure and axis
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    bar_numbers = list(range(len(data_series)))

    # do the bar plot
    bar_plts = []

    for i, ds in enumerate(zip(*data_series)):
        bottoms = [
            sum(prev for prev in data_series[j][:i]) for j in bar_numbers]
        bar_plts.append(
            ax.bar(bar_numbers, ds, bottom=bottoms))

    # label bars
    for bar_debt, name in zip(bar_plts, debt_names):
        for bar in bar_debt:
            txt = plt.text(
                bar.get_x() + bar.get_width()/2,
                bar.get_y() + bar.get_height()/2,
                name,
                ha="center", va="center",
                color="white", fontsize=10, fontweight="bold")
            txt.set_path_effects(
                [patheffects.withStroke(linewidth=2, foreground='black')])

    def lighten(fc):
        ec = [a_c + (1-a_c)*0.75 for a_c in fc]
        ec[-1] = 1
        return tuple(ec)

    # hatching and colors in bars
    plt.rcParams["hatch.linewidth"] = 5
    for bar_debt, color, hatch in zip(bar_plts, colors, hatching):
        for bar in bar_debt:
            bar.set_lw(0)
            bar.set_hatch(hatch)
            bar.set_facecolor(color)
            bar.set_edgecolor(lighten(color))

    # handle axis
    ax.set_xticks(bar_numbers)
    ax.set_xticklabels(bar_labels, weight="bold", fontsize=11)

    ax.set_yticks([0, 25, 50, 75, 100])
    ax.yaxis.set_tick_params(labelsize=10)

    ax.set_ylabel("Proportion of work time, %", weight="bold", fontsize=11)

    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

    ax.tick_params(axis=u'x', which=u'both', length=0)

    ax.set_ylim([0, 100])

    # title
    ax.set_title(graph_title, weight="bold")

    return bar_plts, ax, fig


def add_transition_arrow(bar_plts, ax):

    # transition arrow
    left_bar = bar_plts[0][0]
    left_bar_right = left_bar.get_x() + left_bar.get_width()
    right_bar = bar_plts[0][1]
    right_bar_left = right_bar.get_x()

    arrow_style = patches.ArrowStyle.Simple(head_width=4, tail_width=2)
    arrow = patches.FancyArrowPatch(
        (left_bar_right, 50), (right_bar_left, 50), arrowstyle=arrow_style, mutation_scale=20, color="grey")
    ax.add_patch(arrow)


@dataclass
class NewWork:

    value: int

    name = "New work"
    hatch = "/"
    color = (0.8392156862745098, 0.15294117647058825, 0.1568627450980392, 1.0)


@dataclass
class CodeDebt:

    value: int

    name = "Code debt"
    hatch = "\\"
    color = (0.17254901960784313, 0.6274509803921569, 0.17254901960784313, 1.0)


@dataclass
class Servers:

    value: int

    name = "Servers"
    hatch = "-"
    color = (1.0, 0.4980392156862745, 0.054901960784313725, 1.0)


@dataclass
class Other:

    value: int

    name = "Other"
    hatch = "X"
    color = (0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 1.0)


class WorkTypes:

    def __init__(self, *types):
        self._types = types

    def normalised_data(self):
        data = [t.value for t in self._types]
        prop = 100/sum(data)
        return [prop*d for d in data]

    def names(self):
        return [t.name for t in self._types]

    def hatchings(self):
        return [t.hatch for t in self._types]

    def colors(self):
        return [t.color for t in self._types]


def draw_expected():

    bar_labels = [
        "Before",
        "After\n(Expected)"
    ]

    graph_title = "Expected time spent on catagories of work,\nbefore and after resolving code debt"

    work_before = WorkTypes(NewWork(10), CodeDebt(50), Other(40))
    work_after = WorkTypes(NewWork(55), CodeDebt(5), Other(40))

    bar_plts, ax, fig = draw_tech_debt_plot(
        [work_before.normalised_data(), work_after.normalised_data()],
        bar_labels,
        graph_title,
        work_before.names(),
        work_before.hatchings(),
        work_before.colors()
    )
    add_transition_arrow(bar_plts, ax)
    return fig


def draw_actual():

    work_before = WorkTypes(NewWork(10), CodeDebt(50), Other(40))
    work_after = WorkTypes(NewWork(10), CodeDebt(5), Other(40))

    bar_labels = [
        "Before",
        "After\n(Actual)"
    ]

    graph_title = "Actual time spent on catagories of work,\nbefore and after resolving code debt"

    bar_plts, ax, fig = draw_tech_debt_plot(
        [work_before.normalised_data(), work_after.normalised_data()],
        bar_labels,
        graph_title,
        work_before.names(),
        work_before.hatchings(),
        work_before.colors()
    )
    add_transition_arrow(bar_plts, ax)
    return fig


def draw_with_servers():
    graph_title = "Potential time spent on catagories of work,\nbefore and after resolving server debt"

    bar_labels = [
        "Before",
        "After\n(Potential)"
    ]

    work_before = WorkTypes(NewWork(10), CodeDebt(5), Servers(30), Other(10))
    work_after = WorkTypes(NewWork(10), CodeDebt(5),  Servers(3), Other(5))
    print(work_before.normalised_data())
    print(work_after.normalised_data())

    bar_plts, ax, fig = draw_tech_debt_plot(
        [work_before.normalised_data(), work_after.normalised_data()],
        bar_labels,
        graph_title,
        work_before.names(),
        work_before.hatchings(),
        work_before.colors()
    )
    add_transition_arrow(bar_plts, ax)
    return fig


fig_expected = draw_expected()
fig_expected.savefig("expected.svg")
fig_actual = draw_actual()
fig_actual.savefig("actual.svg")
fig_with_servers = draw_with_servers()
fig_with_servers.savefig("server.svg")

plt.show()
