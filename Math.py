#Math
#Python has a set of built-in math functions, 
#including an extensive math module, that allows you to perform mathematical tasks on numbers.

#Built-in Math Functions
x = min(5, 10, 25)
print(x)
y = max(5, 10, 25)
print(y)
x = abs(-7.25)
print(x)
x = pow(4, 3)
print(x)

#The Math Module
#Python has also a built-in module called math, which extends the list of mathematical functions
import math


x = math.sqrt(64)
print(x)

#The math.ceil() method rounds a number upwards to its nearest integer, 
# and the math.floor() method rounds a number downwards to its nearest integer, and returns the result
x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1
