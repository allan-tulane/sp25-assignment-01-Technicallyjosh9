

# CMPS 2200 Assignment 1

**Name:**Joshua Haddad


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  Yes, 2^(n+1) is O(2^n) because to find if a function is equivalent to its big O time you take the ratio
  - of the fucntion to its big O time. In this case this wold return.  2^(n+1)/ (2^n) which is equivelent to 
  - 2^(n+1) * 2^(-n) which is equivelent to 4. Because this term is not dependent on N we know the two fucntions are equal.
  - 
.  
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  No 2^{2^n} is not equivelnt to 2^{n}.By finding the ratio betweent he two functions and determining if it is still reliant on n we can figure out if they are the same. 
  -2^2^n = 2^2n which divided by 2^n is still 2^n which is a function of n and therefor not equivlent.
.  
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?   
.  No these two functions are not equivalent. n^1.01 is a polynomial function which always scale faster then 
  - logn(n)^2 which is a logarithmic function. Therefor these two functions cannot be equivalent.
.  
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  Yes for n^(1.01) is in Omega(logn(n)^2) This is becase. n^(1.01) always scales quicker than c* (log(n)^2) for any large value of n which satisifies the definition for omega. 
  - Thus n^(1.01) has an equivelnt run time Omega((log(n)^2))
.  
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  No. sqrt(n)= n^(1/2) and log(n)^3 = 3n because when 10 is raised to the log(n) power to cancel out the log of n the function becomes 
  - log(n)^3 = 10^(log(n)^3) which is the same as log(n)^3 = 10^(log(n)*log(n)*log(n)) which is equiveltn to 10^log(n)*3 which is equivelnt to
  - 3n. Therefore because n^(1/2) is an exponentional function where 3n is a polynomial one the logarithmic one
  - scales faster for all values of c in the expression c(3n). This makes the functions un equivalent.
.  
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
 .  Yes, the ratio of sqrt(n)/ (logn)^3 *c is eventually going to results in sqrt(n) dominating (logn)^3 *c over a large enough time span with any value of c.
  - Therfore sqrt(n) is in omega (logn^3).


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  
Done
  - 2b. (6 pts) What does this function do, in your own words?  

.  This function implements the Fibonacci sequence recursively. 
This is done by first establishing a base case of x<=1 which is necissary because the fibonni sequence cannot refrence a negative value so x-2 always has to be greater then zero. 
Then the rest of the seqeunce is generated through finding recursively calling the function foo for values of x-1 and x minus two and adding thme togther. These repeat until x=1 and then return the final value.
Then the function adds all those base values back up in the sequence to get the next value in the series.
.  
.  
.  
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  
Work(n)
W(n) is n because the functions length is determined by the for loop which has to index through all numbers in the list which has a lenght of n. W(n) is equal to the number of vertixes on the tree graph total and there is only one path of length n therefor work must equal length n.
. 
Span(n)
Span(n) is n because there is no parrarellism and the functions entire length is determined by a single for loop which has to index through all the numbers in the list which results in a tree of length n. Span(n) is equal to the total number of nodes along the critical path but because the 
whole tree is a single critical path the span is equal to the length of the tree which as previviously discussed is n.
.  
.  
  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   
Done
  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
  
. The work and span of the sequential algorithm is the same as above because they are the same algorithm. Therfore
.  
.  Work(n):
W(n) is n because the functions length is determined by the for loop which has to index through all numbers in the list which has a lenght of n. W(n) is equal to the number of vertixes on the tree graph total and there is only one path of length n therefor work must equal length n.
. 
Span(n):
Span(n) is n because there is no parrarellism and the functions entire length is determined by a single for loop which has to index through all the numbers in the list which results in a tree of length n. Span(n) is equal to the total number of nodes along the critical path but because the 
whole tree is a single critical path the span is equal to the length of the tree which as previviously discussed is n.
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  
  
.  The work is W(n)= 2W(n/2) + W(1). This is bwecause the list continoally gets divided in half until a 
   base case is reached and then each of these divisions is merged back together which takes W(1). This accounts for both the known and unknown portions of the work

   The span is log_2(n) because the list halves in size after each recurance. So starting of with n//2 for the first reccurance you get n//4 for the second recurance. This gives
   us the general form n//2^(#of recursions).  In the first case n//2^(#of recursions)= 1  therfor n= 2^(#of recursions). Solving for #of recursions we get log_2(n)= number of recursions which is then the value of our span.
.  
.  
.  
.  
.  
.  
.  

