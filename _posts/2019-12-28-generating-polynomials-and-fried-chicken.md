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
	Probability of $$k$$ heads $$=\binom{n}{k}p^{k}(1-p)^{n-k}$$
</p>
This means that if we have $$n=100$$, then we can sum up the "even-headed" outcomes as follows. 
<p style="text-align: center;">
	Probability of even heads $$=\sum_{i=0}^{50}\binom{n}{2i}p^{2i}(1-p)^{n-2i}$$
</p>
I don't know of any clean way to evaluate this summation. 