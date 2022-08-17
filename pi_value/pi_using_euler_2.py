#This pi determination method was proved by gauss and goes like this:
# pi**2/6 = sum_1_to_infinity(1/n**2)

import numpy as np

def pi(iteration):
    sum = 0
    for i in range(iteration):
        sum = sum + 1/(i+1)**2
        pi = math.sqrt(6*sum)
    return pi
