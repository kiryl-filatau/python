def factorial1(x):
    fact = 1
    while x > 1:
        fact *= x
        x -= 1
    return(fact)


x = int(input('please enter a number for factorial1: '))
print(factorial1(x))

########################################

def factorial2(x):
    fact = 1
    for i in range(2, x+1):
        fact *= i
    return(fact)

x = int(input('please enter a number for factorial2: '))
print(factorial2(x))

########################################

def factorial3(n):
    if n == 0:
        return 1
    return factorial3(n-1) * n
 

n = int(input('please enter a number for factorial3: '))
print(factorial3(n))

########################################

import math
n = int(input('please enter a number for factorial_math: '))
print(math.factorial(n))