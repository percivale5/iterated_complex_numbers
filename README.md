# Probability of the Location of the End Points of Iterated Circular Complex Numbers
Investigating the probability of the location of the end points of iterated complex numbers on the unit circles. Began as my IB Mathematics AA HL Internal Assessment (IA), continuing the inquiry here.

In [my IA](https://github.com/percivale5/iterated_complex_numbers/blob/main/SamMorrisAAHL_IA2026.pdf), I lay out, in the context of the project, the background and the research question, and propose a conjecture. Terminology and method used here may differ from what is in the IA, being in a different context.

## Background/Question Summary
To a complex number $z_1$ randomly selected on the unit circle centered at the origin $z=1$ add another complex number $z_2$ randomly selected on the unit circle centered at $z_1$. The number (or rather, set of possible numbers) $z_2$ is an **iterated circular complex number**. This process can be repeated $n$ times to get the general iterated circular complex number, $z_n$. The general iterated ciruclar complex number is defined more formally and in many ways:
$$
z_n=\sum_{x=1}^{n}\text{cis}(\alpha_x)=\sum_{x=1}^{n}e^{i\alpha_x}=z_{n-1}+e^{i\alpha_n}
$$
where $\alpha_x$ is a continuous random variable that uniformly takes on a value in the interval $[0,2\pi)$ for each $x$, and does so independently of all other values of $\alpha_x$. 

Now, I ask:
<div align="center">

**What is the probability that $z_n$ falls within but not on the unit circle $|z|=1$ for a given $n$?**

</div>
This is equivalent to finding the following probability:
$$
P(|z_n|<1)
$$
And for conciseness, this statement will be referred to as $P(Z_n)$.

## Conjecture
It is easily provable that $P(Z_2)=\frac{1}{3}$, and I contstructed samples by way of simulation to reasonably form a basis for the following conjecture:
$$
P(Z_n)=\frac{1}{n+1}
$$

The code used in the IA is found in the document's appendix and as .py files here: [still need to add them :\(...].