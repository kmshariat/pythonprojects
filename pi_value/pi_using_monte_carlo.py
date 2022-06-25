import random

pt_in = 0 #points inside the quarter circle
pt_t = 0 #points inside the whole quarter square

n = int(input("How many iterations do we want? "))

for i in range(n):
  x = random.uniform(0,1) #random.uniform(a,b) takes a random uniformly distributed number between a and b
  y = random.uniform(0,1)
  if x**2+y**2 <= 1: #x**2 + y**2 <=1 justifies if the point is inside the circle or not
    pt_in +=1 
  pt_t +=1
  
print(4*(pt_in/pt_t)) 
