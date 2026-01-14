def fact_num(n):
    if n==0:
        return 1
    else:
        fact=n*fact_num(n-1)
        return fact

n=int(input("enter number:"))
print(fact_num(n))

import math

# Input number
num = float(input("Enter a number: "))

# Calculations using math module
square_root = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)

# Output results
print("Square root:", square_root)
print("Natural logarithm (log base e):", natural_log)
print("Sine (in radians):", sine_value)
