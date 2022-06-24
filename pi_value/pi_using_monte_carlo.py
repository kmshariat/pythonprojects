#unfinished
import random
x = random.uniform(0,1)
y = random.uniform(0,1)
pt_in = 0.0
pt_t = 0.0
for i in range(1000):
    if x**2+y**2 < 1:
        pt_in +=1
    pt_t +=1
print(pt_in/pt_t)
