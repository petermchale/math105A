# Math 105A Numerical Analysis 

Instructor: Peter McHale 

Course webpage: https://eee.uci.edu/17f/44635

## Getting set up for the Lab section

In what follows, you will need to access the 'command line'. 
On a Mac, this is done by opening the `Terminal` app. On the lab (Windows) machines,
this is done via `Start` -> `Anaconda Prompt` (type this into the search field to locate the program). 
Your TA will help you with this. 

If on your own machine, install Python and Jupyter by installing 
[Anaconda](https://www.continuum.io/downloads) (Python 3.x version).
 Anaconda conveniently installs Python, the Jupyter Notebook, and other commonly used packages for scientific computing.

If you are working at a lab computer, which already has Python and Jupyter installed, then 
type `python --version` at the command prompt to 
check the version of Python that is installed. It will probably say Python 2.x. I am using Python 3.x. 
The differences are not large, so you could go ahead and use Python 2.x. 
Alternatively, you could 
[create a conda environment](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands) and [activate it](https://conda.io/docs/user-guide/tasks/manage-environments.html#activating-an-environment).
However, I am not sure that this environment will persist between login sessions. 
Your TA will help you with this. 

Open a Jupyter notebook by navigating to the directory in which it is located (the `cd` command is useful here, 
as is the `ls` command in `Terminal` or equivalently, the `dir` command in Windows)
and typing `jupyter notebook <notebook name>` at the 
command prompt. Seek out the TA for help.

Once you’re finished editing/running your notebook, press `ctrl-c`
twice at the command prompt.

If Jupyter complains that a specific package is missing when you 
run your notebook, then return to the command line, execute 
`conda install <name of package>`, and re-run the offending notebook cell. 

## Acknowledgements 

This course is adapted from [Tom Trogdon's course](https://www.math.uci.edu/~ttrogdon/105A/html/MATH105A.html).

## Schedule
In the table below, `Sections` refers to sections of *Numerical Analysis, R.L. Burden and J.D. Faires, 9th Edition*

Click on the links to see nbviewer-rendered versions of the lecture. 

|Wk|Date|Lec|Sections|Topics
|---|---|---|---|---
|0|9/29|1|1.1|[Review of calculus](http://nbviewer.jupyter.org/github/petermchale/math105A/blob/master/lectures/Lecture1.ipynb)
|1|10/2|2|1.2|[Round-off errors and computer arithmetic](http://nbviewer.jupyter.org/github/petermchale/math105A/blob/master/lectures/Lecture2.ipynb)
||10/4|3|2.1|Bisection Method
||10/6|4|2.2|Fixed-point iteration
|2|10/9|5|2.3|Newton’s method
||10/11|6|2.4/2.5|Error analysis/Convergence
||10/13|7|2.6|Zeros of polynomials
|3|10/16|8|6.1|Gaussian elimination
||10/18|9|6.1|Algorithm complexity
||10/20|10|6.2|Pivoting strategies
|4|10/23|11|6.2|Pivoting strategies (continued)
||10/25|12|6.3-6.4|Matrix Inversion; Determinants
||10/27|13|6.5|LU factorization
|5|10/30|14|6.6|Other factorizations
||11/1|||Review of previous exams
||11/3||1, 2, 6|Midterm Exam
|6|11/6|15|7.1|Norms of vectors and matrices
||11/8|16|7.2, 9.1|Spectral radius of a matrix
||11/10||No class|Veterans’ Day
|7|11/13|17||Existence and speed of convergence
||11/15|18|7.3|Jacobi and Gauss-Siedel
||11/17|19|7.4|Accelerating convergence
|8|11/20|20||Applications of Linear Systems
||11/22|21|9.1 - 9.3|Orthogonality (Gram Schmidt), Similarity, Power Method
||11/24||No class|Thanksgiving
|9|11/27|22|9.3|Power method (continued)
||11/29|23|9.5|QR algorithm
||12/1|24|9.6|SVD
|10|12/4|25|9.6|SVD (continued)
|9|12/6|26||Applications of SVD
||12/8|27||Review of previous exams
|11|12/11||1, 2, 6, 7, 9|Final Exam 1.30pm – 3.30pm

