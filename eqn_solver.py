#Solving equations using kramers method upto three variable
var = int(input("How many variables? (range 1-3) "))
if var == 1:
  print("Equation to follow: a x = c")
  print("-"*30)
  a = float(input("Enter a "))
  c = float(input("Enter c "))
  if a == 0:
    print("Undefined")
  else:
    x = c/a
    print(f"Solution x = {x}")
elif var == 2:
  print("Equation to follow:")
  print("a1 x + b1 y = c1 ")
  print("a2 x + b2 y = c2 ")
  print("-"*30)
  a1 = float(input("Enter a1 "))
  b1 = float(input("Enter b1 "))
  c1 = float(input("Enter c1 "))
  a2 = float(input("Enter a2 "))
  b2 = float(input("Enter b2 "))
  c2 = float(input("Enter c2 "))
  d = a1*b2 - a2*b1
  if d == 0:
    print("Undefined")
  else:
    dx = c1*b2-c2*b1
    dy = a1*c2- a2*c1
    x= dx/d
    y = dy/d
    print(f"Solutions (x,y) = ({x},{y})")
elif var == 3:
  print("Equation to follow:")
  print("a1 x + b1 y + c1 z = p1 ")
  print("a2 x + b2 y + c2 z = p2 ")
  print("a3 x + b3 y + c3 z = p3 ")
  print("-"*30)
  a1 = float(input("Enter a1 "))
  b1 = float(input("Enter b1 "))
  c1 = float(input("Enter c1 "))
  p1 = float(input("Enter p1 "))
  a2 = float(input("Enter a2 "))
  b2 = float(input("Enter b2 "))
  c2 = float(input("Enter c2 "))
  p2 = float(input("Enter p2 "))
  a3 = float(input("Enter a3 "))
  b3 = float(input("Enter b3 "))
  c3 = float(input("Enter c3 "))
  p3 = float(input("Enter p3 "))
  d = a1*(b2*c3-c2*b3)-b1*(a2*c3-c2*a3)+c1*(a2*b3-b2*a3)
  if d==0:
    print("Undefined")
  else:
    dx = p1*(b2*c3-c2*b3)-b1*(p2*c3-p3*c2)+c1*(p2*b3-p3*b2)
    dy = a1*(p2*c3-p3*c2)-p1*(a2*c3-a3*c2)+c1*(a2*p3-a3*p2)
    dz = a1*(b2*p3-b3*p2)-b1*(a2*p3-a3*p2)+p1*(a2*b3-a3*b2)
    x = dx/d
    y = dy/d
    z = dz/d
    print(f"Solutions(x,y,z) = ({x},{y},{z})")
