---
layout: post
title: Generating polynomials and fried chicken
published: true
---

<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
});
</script>

It was a Spring Friday evening in 2018, and it was towards the end of the weekly CS70 staff meeting. Everyone was excited, as the professor usually ordered some pizza for us. This time, however, we got Korean fried chicken, so I must imagine that some billionaire decided to randomly donate to the CS departmental budget. As I am munching on the the fattest drumstick that I can recall in recent memory, my friend poses the following question:

> If I flip a coin 100 times, what is the probability that it lands heads an even number of times?

My first instinct was $$\frac{1}{2}$$, but there are 51 outcomes for even, and 50 outcomes for odd. I think about it for a little longer, and start writing out the summation of binomial coefficients that sums all probability of even outcomes. Before I can finish though, another friend (the head TA) comes up behind us, thigh in hand, and says:

> "Insert exact answer"

When flipping a coin with bias $$p$$ a total of $$n$$ times, we know that the probability for $$k$$ heads will follow a binomial distribution. 
<p style="text-align: center;">
	$$\text{Probability of $$k$$ heads}=\binom{n}{k}p^{k}(1-p)^{n-k}$$
</p>
This means that if we have $$n=100$$, then we can sum up the "even-headed" outcomes as follows. 
<p style="text-align: center;">
	$$\text{Probability of even heads} =\sum_{i=0}^{50}\binom{n}{2i}p^{2i}(1-p)^{n-2i}$$
</p>
I don't know of any clean way to evaluate this summation. 

There is a way to solve this by defining a recursive relationship. If we have 

> Roots of unity: The solutions to the equation $$x^2=1$$ are $$x=e^{\frac{2\pi}{2}},e^{\frac{2\pi}{1}}=1,-1$$. If we set $$\omega=e^{\frac{2\pi}{2}}$$, then $$\omega, \omega^2$$ are called the roots of unity when $$n=2$$. For any $$n$$, the roots of unity sum to zero. 

If you feel like I am pulling this out of my hat, well then you are right, but stay with me now. Let's go deeper into the territory of seemingly baseless calculations, and do $$(1+\omega)^n+(1+\omega^2)^n$$, which, using a binomial expansion, we see evaluates to:

<p style="text-align: center;">
	$$(1+\omega)^n+(1+\omega^2)^n=[\binom{n}{0}\omega^0+\binom{n}{1}\omega^1+\binom{n}{2}\omega^2...]+[\binom{n}{0}\omega^{0}+\binom{n}{1}\omega^2+\binom{n}{2}\omega^4...]$$
	$$=[2\binom{n}{0}+\binom{n}{1}(\omega^1+\omega^2)+\binom{n}{2}(\omega^2+\omega^4)...]$$
</p>

The important part about the resulting sum is that *the odd terms will go to zero* and *the even terms are untouched*. This is known as the roots of unity filter, and we can utilize it to solve our problem. 

<p style="text-align: center;">
	The number of ways that 
</p>