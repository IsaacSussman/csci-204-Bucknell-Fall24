import matplotlib.pyplot as plt
import math

"""
The domain of your plots.
"""
DOMAIN = 10

"""
The following function plots any recurrence relation you give it. 
For example, if I wanted to plot the recurrence relation f(n), I would call plot_me(f).
"""
def plot_me(f) :
    grph = [f(i) for i in range(DOMAIN)]
    plt.plot(grph, label="Recurrence")

def plot_me_minus(f) :
    grph = [f(i) for i in range(DOMAIN)]
    plt.plot(grph, label="Recurrence")

"""
O( - ) types
The following 5 functions plot a function that might go in an O(-). 
You need to supply the function with a constant multiple (a) and a constant (c) that it starts from.
For example, polynomial(5, 10, 1) plots the line with slope 5 and y-intercept 10.
"""
def constant(c) :
    """
    Plots f(n) = c, representing O(1)
    """
    grph = [c for i in range(DOMAIN)] 
    plt.plot(grph, label="Constant")
    
def polynomial(a, c, k)	:
    """
    Plots f(n) = a n^k + c, representing O(n^k)
    """
    grph = [a * (i ** k) + c for i in range(DOMAIN)]
    plt.plot(grph, label=f"n^{k}")

def exponential(a, c, b) :
    """
    Plots a (b^n) + c, representing O(b^n)
    """
    grph = [b ** i for i in range(DOMAIN)] 
    plt.plot(grph, label=f"{b}^n")

def logarithmic(a, c)	:
    """
    Plots a log(n) + c, representing O(log(n))
    """
    grph = [0] + [a * math.log2(i) + c for i in range(1, DOMAIN)] 
    plt.plot(grph, label=f"log(n)")	

def nlog(a, c) :
    """
    Plots a n log(n) + c, representing O(nlog(n))
    """
    grph = [0] + [a * i * math.log2(i) + c for i in range(1, DOMAIN)] 
    plt.plot(grph, label=f"nlog(n)")	

"""
You can put your recurrence relations below if you like 
"""
def f_1(n) :
    return 2

def f_3(n):
    if n==0:
        return 2
    elif n<0:
        return 3+f_1(n+1)
    else:
        return 3+f_3(n-1)
    
def f_4(n):
    if n <= 1:
        return 3
    else:
        return 9+n-2+f_4(n-2)
    
def f_5(n):
    if n<=1:
        return 13
    else:
        return 2+f_5(n-1)

def f_6(n):
    if n<=0:
        return 2
    else:
        total = 0
        for i in range(n):
            total += 1
        return n*2+3 + f_6(n-1)

def f_7(n):
    if n <= 0:
        return 2
    else:
        t = 0
        for i in range(n):
            for j in range(i):
                t += 3
        return t + 2 + f_7(n-1)

def f_8(n):
    if n==0:
        return 2
    else:
        return f_7(n-1) + f_8(n-1) + 2

def f_9(n):
    if n==0:
        return 3
    else:
        return 6 + 4*2**(n-1) + f_9(n-1) - 1
    
def f_10(n):
    if n<= 1:
        return 2
    else:
        return 2+f_10(n//2)

def f_11(n):
    if n<= 1:
        return 2
    else:
        return 3 + f_11(n//2) + f_11(n//2)

def f_12(n):
    if n== 0:
        return 2
    else: 
        total = 0
        return 4 + n*2 + f_12(n//2)
def f_13(n):
    if n<=1:
        return 2
    else:
        return 2 + f_13(n//2) + f_13(n//3)

""" 
The following code demonstrates plotting the O(-) functions.
You should comment them out and keep only the ones you are working with.
"""
#constant(1)             # Constant Time
#polynomial(1, 0, 1)     # Linear Time
#polynomial(1, 0, 2)     # Quadratic Time
#polynomial(1, 0, 3)     # Cubic Time
polynomial(1, 0, 4)
#exponential(1, 0, 2)    # Exponential Time
#logarithmic(1, 0)       # Logarithmic Time
#nlog(1, 0)              # Logarithmic Time

plot_me(f_8)            # Recurrence Relation

### Show your plots (KEEP THIS):
plt.xlabel("Size of input")
plt.ylabel("# of steps")
plt.legend()
plt.show()
