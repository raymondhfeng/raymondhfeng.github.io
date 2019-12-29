---
layout: post 
title: Second Order Cone Programming
published: true
---
## Second Order Cone Programming

<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
});
</script>
<h4>Motivation</h4>
Second Order Cone Programming is a powerful tool. This convex optimization problem has the form:
<p style="text-align: center;">
$$\text{min}_{x \in \mathbb{R}^n} c^Tx$$
$$\text{s.t. } \|A_ix+b_i\|_2 \leq c_i^Tx+d_i$$
</p>
There are many optimization problems that can be reduced to this general form, but the punchline is, we now allow for constraints involving the norm of $x$, a step up from the linear constraints that we required in LPs, and QPs. But it is not obvious why SOCPs are more "general" than QCQPs, which have the form:
<p style="text-align: center;">
$$\text{min}_{x \in \mathbb{R}^n} x^TH_0x+2c_0^Tx+d_0$$
$$\text{s.t. } x^TH_ix+2c_i^Tx+d_i \leq 0$$
$$x^TH_jx+2c_j^Tx+d_j = 0$$
</p>
Can't we just square the inequality constraint in our SOCP, such that it can be massaged into a QCQP? This is not the case, because in general, it is invalid to square constraints of the form $\|x\| \leq k$. So SOCP is at least as general as QCQP. 

<h4>Terminology</h4>
What is a cone? The definition of a cone is any set $\mathcal{S}$ that satisfies the property that $$s \in \mathcal{S} \Rightarrow \alpha s \in \mathcal{S}, \alpha \geq 0$$. There are all types of different cones that topologists love to study, but we will look at the "norm cone" with respect to a norm $$\|*\|$$:
$$\mathcal{C}=\{(x,t), \|x\| \leq t\} \subseteq \mathcal{R}^{n+1}$$ 
We mathematically define an $(n+1)$ dimensional Second Order Cone as follows:
$$\mathcal{K}_n=\{(x,t),x \in \mathbb{R}^n, t \in \mathbb{R}: \|x\|_2 \leq t\}$$
Here, we see the meaning of the name "Second Order" cone, as it is a norm cone using the $$\mathcal{l}_2$$ norm. Another equivalent definition of the $(n+1)$ second order cone is the intersection of an infinite number of half spaces:
$$\mathcal{k}_n=\bigcap_{u:\|u\| \leq 1}\{(x,t), x \in \mathbb{R}^n, t \in \mathbb{R} : x^Tu \leq t\}$$