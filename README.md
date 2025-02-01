# Project Submission for Topological Data Analysis

This repository contains my group's submission for a small project conducted as part of one of our second-year computer science course. The goal of this project is to manipulate, at a very low level, essential tools in topological data analysis, such as **Čech complexes** and **α-complexes**.

## Overview

To study these complexes, we devised an algorithm to compute the **Minimal Enclosing Ball (MEB)** of a set of multi-dimensional points. To achieve this, we used **Welzl's LP-type algorithm** (see [`meb/`]([meb/](https://github.com/ArnaudoB/Intro-To-Topological-Data-Analysis/tree/master/meb))).  

- In [`naive_simplexes/`]([naive_simplexes/](https://github.com/ArnaudoB/Intro-To-Topological-Data-Analysis/tree/master/naive_simplexes)), we **naively** enumerate the simplexes of dimension at most *k* and filtration value at most *l* of the **Čech complex** of a set of points using a backtracking algorithm.  
- In [`simplexes/`]([simplexes/](https://github.com/ArnaudoB/Intro-To-Topological-Data-Analysis/tree/master/simplexes)), we **optimize** this algorithm by eliminating unnecessary explorations.  
- In [`alpha_complexes/`]([alpha_complexes/](https://github.com/ArnaudoB/Intro-To-Topological-Data-Analysis/tree/master/alpha_complexes)), we enumerate the simplexes of dimension at most *k* and filtration value at most *l* of the **α-complex** of a set of points.

## Visualization

The folder [`plot_simplexes/`]([plot_simplexes/](https://github.com/ArnaudoB/Intro-To-Topological-Data-Analysis/tree/master/plot_simplexes)) contains a **visualization tool** for plotting a given set of points and a corresponding set of simplexes (limited to 3D).  

## Testing

Each folder includes a [`test/`] subdirectory containing **unit tests** for the functions and, in some cases, plots.

