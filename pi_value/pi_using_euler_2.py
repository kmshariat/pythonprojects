#This pi determination method was proved by gauss and goes like this:
# pi**2/6 = sum_1_to_infinity(1/n**2)

import numpy as np

sum = 0
for i in range(10000):
  sum = sum + 1/((i+1)*(i+1))

print(f"pi is almost equal to : {np.sqrt(sum*6)}")
