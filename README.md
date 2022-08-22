# Black Holes Game Test Assignment
Yet Another Test Assignment

## How to run:
1. Clone the repo
2. Install the requirements via ```pip install -r requirements.txt```
3. Run test script via ```python main.py```

## Part 1:
I chose Numpy multi-dimensional arrays as most convenient data structure for storing the basic field functionality.
It brings clear and widely known API for this solution and allows you to vectorize your code if needed, which i used in view_field.py with matrix convolution trick for neighbours counting.
As an alternative i can suggest using some linked data structures like Queues or even Multi-Linked Lists. But, i believe, they are not so intuitive when it comes to maintainability part of the solution, and the implementation with NumPy seems more domain-driven.

Overall, solution follows the layered architecture pattern:

Black Holes Matrix -> Neighbours Count Matrix -> Iteratively Updated Visibility Matrix -> View method (show_field in GameField class)

## Part 2:
This is very simple: you just need to create zero matrix, substitute some values with ones and redistribute them among matrix in random manner. 

## Part 3:
Here convolution were used. I decided to avoid the procedural code as long as possible 'cause it helps to leverage the vectorized computations potential.

## Part 4:
Here i used a recursive solution for making every needed cell visible as most convenient and intuitive solution. It got clear break conditions, so there shouldn't be any endless recursion cases.
