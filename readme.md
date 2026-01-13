Simple Linear Regression From Scratch (Pure Python)
Project Overview

This repository contains a from-scratch implementation of Simple Linear Regression using pure Python, without relying on NumPy, Pandas, or any machine learning libraries.

The objective of this project is to expose the raw mechanics of machine learning, showing how a model learns by iteratively reducing error using gradient descent. Every calculation is done explicitly using Python lists, loops, and arithmetic operations.

This project intentionally avoids abstractions to ensure full transparency of the learning process.

Why This Project Matters

Modern ML frameworks hide the learning process behind APIs.
This project removes that veil.

By writing linear regression manually, this repository demonstrates:

How models learn through error minimization

How gradients guide learning

Why optimization is just math + iteration

That machine learning works even without libraries

If you understand this code, you understand the core logic behind all supervised learning models.

Problem Statement

Given a set of input values 
𝑥
x and corresponding outputs 
𝑦
y, the goal is to learn a function that best fits the data and can predict unseen values.

Dataset Used
x = [1, 2, 3, 4, 5]
y = [10000, 8000, 6000, 4000, 2000]


This dataset follows a perfectly linear downward trend, making it ideal for demonstrating gradient descent convergence.

Model Assumption

The model assumes a linear relationship between input and output.

Linear Equation
𝑦
^
=
𝑚
𝑥
+
𝑐
y
^
	​

=mx+c

Where:

𝑚
m is the slope (weight)

𝑐
c is the intercept (bias)

𝑦
^
y
^
	​

 is the predicted output



The algorithm adjusts the line until it best fits all data points.

Loss Function: Mean Squared Error (MSE)

To measure how wrong the model is, we compute Mean Squared Error:

𝑀
𝑆
𝐸
=
1
𝑛
∑
𝑖
=
1
𝑛
(
𝑦
𝑖
−
𝑦
^
𝑖
)
2
MSE=
n
1
	​

i=1
∑
n
	​

(y
i
	​

−
y
^
	​

i
	​

)
2

Why square the error?

Penalizes large mistakes

Ensures non-negative values

Smooth gradient for optimization

The entire training process exists to minimize this value.

Optimization: Gradient Descent

Gradient Descent is the algorithm that updates the parameters 
𝑚
m and 
𝑐
c to reduce error.

Gradients

Slope gradient:

∂
𝐸
∂
𝑚
=
−
2
𝑛
∑
𝑥
𝑖
(
𝑦
𝑖
−
𝑦
^
𝑖
)
∂m
∂E
	​

=−
n
2
	​

∑x
i
	​

(y
i
	​

−
y
^
	​

i
	​

)

Intercept gradient:

∂
𝐸
∂
𝑐
=
−
2
𝑛
∑
(
𝑦
𝑖
−
𝑦
^
𝑖
)
∂c
∂E
	​

=−
n
2
	​

∑(y
i
	​

−
y
^
	​

i
	​

)

These gradients indicate:

Direction of steepest error increase

How much each parameter contributes to the error

Parameter Update Rule

After computing gradients, parameters are updated as:

𝑚
=
𝑚
−
𝛼
⋅
∂
𝐸
∂
𝑚
m=m−α⋅
∂m
∂E
	​

𝑐
=
𝑐
−
𝛼
⋅
∂
𝐸
∂
𝑐
c=c−α⋅
∂c
∂E
	​


Where:

𝛼
α is the learning rate

This process is repeated over many iterations (epochs).

Training Process

The script follows this exact loop:

Initialize slope and intercept to zero

Loop over epochs

For each data point:

Compute prediction

Compute error

Accumulate gradients

Update parameters

Repeat until convergence

This loop is the core learning engine of machine learning.

Code Structure

Data initialization using Python lists

Manual gradient calculation

Explicit parameter updates

Final prediction using trained values

No hidden functions. No abstractions.

Results

After 1800 epochs, the model converges to:

Slope (m): approximately -2000

Intercept (c): approximately 12000

Prediction Example

For input 
𝑥
=
3
x=3:

𝑦
^
=
(
−
2000
×
3
)
+
12000
=
6000
y
^
	​

=(−2000×3)+12000=6000

Which matches the true value exactly.

Requirements

Python 3.x

No external libraries required

This code runs anywhere Python runs.

Learning Outcomes

This project builds a strong understanding of:

Linear regression fundamentals

Loss functions

Gradient descent mechanics

Parameter optimization

Mathematical thinking in ML

Everything you need before touching advanced models.

Future Extensions

Add visualization of loss over epochs

Extend to multivariable linear regression

Implement batch vs stochastic gradient descent

Compare with NumPy-based implementation
