---
layout: post
title: Some comments on the mod-math section
published: true
---

<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
});
</script>

Dear students,

 

As I said in lecture, this segment on mod math and its applications is the heart of the discrete-math part of the course, and represents the biggest module in this section. It is also the part that is essentially always taught in 70 and with essentially this same application scope (RSA, Secret-Sharing, and Reed-Solomon style Error-Correcting Codes) --- everything else in this discrete math section is sometimes skipped/shrunk/expanded/etc. In a way, you can think about the first set of material on proofs as sharpening the underlying skills, and the earlier stuff on Stable Matchings and Graphs as making sure you've practiced the skills enough to be able to handle what's happening here and beyond. Consequently, this is also the section where the "mathematical maturity" background is really playing a significantly bigger role. Why? Because the objects and ideas of interest intrinsically build on your mathematical foundations much more than the Matchings or Graph material does. 

 

So, in response to privately-asked student questions, I wanted to quickly describe some of this. After all, it is our belief that everything here should be accessible to a hard-working student with the appropriate background. We don't want students to feel discouraged and doubt their abilities when in fact, the problem is simply one of rusty background. 

## RSA

To understand RSA (as opposed to merely following along), the biggest piece of mathematical maturity background that is critical is the appreciation for the idea of the power of the "right" coordinate systems. In the case of RSA, that "right" coordinate system is provided by the CRT. The importance of getting the coordinate system right is of course one of the dominant themes of EECS16B, where this comes up again and again in diverse contexts, but always using familiar numbers like Real or Complex numbers. (It takes repetition to build maturity.) The second important maturity ingredient is the crucial importance of understanding behavior in the simple case. For RSA, the critical behavior is that of exponentiation --- namely its potential to be periodic. And FLT provides the insight into this for the case of a prime modulus. We anticipate that students will have come to internalize this combination in a course like EECS16B where they learned how to solve linear differential equations --- first in the simple scalar case (where amazingly, the relevant concept also turned out to be exponentiation!), and then leveraging this using the right coordinate system to attack systems of linear differential equations. The overall thought pattern is expected to be similar, but the underlying pieces are different. 

 

Covering RSA in one lecture (as 70 has essentially always done) is only really possible under the assumption that this underlying maturity exists. Without it, students would be getting hit at multiple levels --- not only would RSA be new, but the thought-pattern being followed would also be new. That can be really hard to take in without feeling like you're going under water. It's challenging enough with the underlying thought pattern in your repertoire. 

 

The CRT itself is again something that leans on underlying mathematical maturity. There is the general desire to sniff out the right coordinate system (described above), but even beyond that, there is the desire for coordinates at all. The power of coordinates and the vector view is something that is hit constantly in EECS16AB --- so much so that it almost becomes part of the ambient atmosphere. This becomes a part of mathematical maturity and allows students to perceive the *absence* of coordinates and miss them for modulo arithmetic, thereby helping understand the need for the CRT. The underlying maturity that comes from experience with taking linear combinations is what the exposition of the EGCD and transition to CRT implicitly leans upon --- after all, the EGCD is clearly about taking integer linear combinations of numbers. And of course, the actual construction of the basis numbers in the CRT clearly rhymes with the Lagrange interpolation of polynomials taught in EECS16B.

 

The bigger point here is that the underlying maturity changes the entire character of how the CRT is accepted. With the maturity, it feels like a breath of air. You can get orientation and perspective on mod math when the numbers are not prime. It makes sense to work in coordinates that respect the structure of what is going on. Without the maturity, it would feel like yet another thing in a succession of things that seem like they have nothing to do with each other except the word "mod."

 

I went a bit slower through all this material in lecture and discussion because I wanted to make sure that folks got it. Sometimes 70 powers through things faster because many people take the maturity so much for granted that it is not even worth pointing out obvious things. Having taught the freshman courses, I lean towards going slowly and reminding people.

 

Secret Sharing: Here, the dependence on maturity is even more overt. The "information as degrees of freedom" orientation that students learn in EECS16A right from the beginning is pervasive. There is obviously also the polynomials and Lagrange Interpolation itself from EECS16B. After all, in 16B (and even a bit in 16A actually!) we talk about going from evaluations to polynomial coefficients and vice-versa.  The treatment here in 70 is about verifying that familiar polynomial properties keep working in finite fields (working with numbers mod a prime number), while taking the opportunity to firm up those foundations along the way. And then seeing how these properties give us what we want for secret sharing. Along the way, we use counting to better appreciate the finiteness of the objects here and also make a connection between polynomials and division/modulo itself. All these latter things are the 70 stuff --- most of the underlying polynomial stuff is essentially a part of assumed maturity. Again, how could this possibly be done in one lecture and one discussion otherwise? 

 

Error Correcting Codes: At this point, the dependencies are entirely out in the open and unmistakable. The entire story is always about using systems of linear equations to do what we want to do, so that Gaussian Elimination can do the work for us. Everything is about recapitulating the broad arc of EECS16A Modules 1&3, except in finite fields. We know how to solve systems of linear equations where there are no errors as long as we have enough equations. How do we do this when there are errors? Students are expected to have seen in EECS 16A how a generic assumption on the "smallness" of the errors is translated into mathematics, and then how the problem turns into solving an appropriate system of linear equations. Along the way, they've already seen how dealing with errors naturally needs more equations than true unknowns. However, in the simpler setting of EECS 16A, the natural *geometry* of real spaces is used in a vital way to derive least squares. (And EECS 16B gives students plenty more practice and engagement with least squares and related thinking --- after all EECS 16AB are essentially machine learning foundations courses and this stuff is absolutely foundational --- hit in lab, project, python code, proofs, etc.) Here in 70, we are denied that particular geometry and so need to do something different. The whole story of this in 70 recapitulates conceptual steps that are intended to be familiar, except with the twists needed to deal with errors in this context. Here, those twists have to rely vitally on the structured nature that polynomials provide whereas in EECS 16A, the story could be more general for the real setting. 

 

Once again, this is a story that is typically done in 70 in a single lecture. (I'll go a bit slower.) Why? Because with the background, the actually new 70-esque things that are happening are not that many. Students are expected to have a background that has already internalized systems of linear equations, least squares, etc. 

 

The payoff of course is massive. RSA, secret sharing, and polynomial-based error-correction are all ideas that no amount of mere hacking or tinkering could ever have come up with. These showcase the incredible power of the ways of thinking that previous courses have equipped you with and that we are trying to build upon. (Figuratively standing on the shoulders of giants.) Of course, this only works if the story is actually understood! 

 

I hope that this post helps students that might want to brush up on the relevant ideas. As I've been doing, I'll point out connections overtly in lecture as well. But the course intrinsically proceeds on the assumption that the background is entirely internalized by this point.