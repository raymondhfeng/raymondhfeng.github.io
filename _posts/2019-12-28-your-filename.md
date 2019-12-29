---
layout: post 
title: just a test
published: true
---
## A New Post

this is my second post, hoopla.
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
});
</script>
<h4>Motivation</h4>
Second Order Cone Programming is a powerful tool. This convex optimization problem has the form:
$$\text{min}_{x \in \mathbb{R}^n} c^Tx 
\text{s.t. } \|A_ix+b_i\|_2 \leq c_i^Tx+d_i$$
There are many optimization problems that can be reduced to this general form, but the punchline is, we now allow for constraints involving the norm of $x$, a step up from the linear constraints that we required in LPs, and QPs. But it is not obvious why SOCPs are more "general" than QCQPs, which have the form:
$$\text{min}_{x \in \mathbb{R}^n} x^TH_0x+2c_0^Tx+d_0 \\ 
\text{s.t. } x^TH_ix+2c_i^Tx+d_i \leq 0 \\
x^TH_jx+2c_j^Tx+d_j = 0$$
Can't we just square the inequality constraint in our SOCP, such that it can be massaged into a QCQP? This is not the case, because in general, it is invalid to square constraints of the form $\|x\| \leq k$. So SOCP is at least as general as QCQP. 