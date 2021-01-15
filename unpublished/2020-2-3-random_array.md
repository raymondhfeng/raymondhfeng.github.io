---
layout: post
title: Random Array Generating Processes
published: true
---

<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
});
</script>


## Problem 1

Suppose you generate an array of 100 integers A in the following way:
- At index i, generate a random integer which is uniform[currentMax, 1000]
- Update the currentMax
- Increment i and loop until done

What does the distribution of these arrays look like. Is it uniformly distributed?

## Problem 2

Suppose you are generating an array of tuples in the following manner:
- At index i, generate a random tuple from two normal distributions...

## Programming and Mathematical Analysis

Sharp orders and non-sharp orders

