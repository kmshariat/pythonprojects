#Program to solve quadratic equation
import math
print("Given form of the eqn: ax^2 + bx + c = 0")
print("-"*30)
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
d = b**2 - 4*a*c
if d<0:
  print("Imaginary domain")
elif d==0:
  x = -(b/(2*a))
else:
  sqd = math.sqrt(d)
  x1 = (-b+sqd)/(2*a)
  x2 = (-b-sqd)/(2*a)
  print(f"Solutions are: {x1} and {x2}")
