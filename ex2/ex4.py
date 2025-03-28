# Author: Damian Zukowski 

import math

def factorials(n: int):
    fact_value = math.factorial(n)
    return {n: fact_value}

print("Factorial of 5: ", factorials(5))
