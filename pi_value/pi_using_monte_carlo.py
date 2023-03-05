import random
import matplotlib.pyplot as plt
import numpy as np

pt_in = 0 #points inside the quarter circle
pt_t = 0 #points inside the whole quarter square

n = int(input("How many iterations do we want? "))

#array for storing values of psedu-random values
x_value = [] 
y_value = [] 
pi = []

for i in range(n):
  x = random.uniform(0,1) #random.uniform(a,b) takes a random uniformly distributed number between a and b
  y = random.uniform(0,1)
  x_value.append(x) 
  y_value.append(y) 
  if x**2+y**2 <= 1: #x**2 + y**2 <=1 justifies if the point is inside the circle or not
    pt_in +=1 
  pt_t +=1
  pi.append(4*(pt_in/pt_t))
 
#Generating A Circle's one-fourth
x_circ = np.linspace(0,1,1000) 
y_circ = np.sqrt(1-x_circ**2) 

plt.figure(figsize=(10,5))
plt.subplot(1,2,2)
plt.plot(np.linspace(0,1,n),pi)
plt.title('Value of Pi in each iteration')

plt.subplot(1,2,1)
plt.plot(x_circ,y_circ,color='red')
plt.scatter(x_value, y_value, marker="+")
plt.title('Points inside and outside the circle')

plt.show()
