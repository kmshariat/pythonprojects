# A program to determine the position of a point in 2 D space
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
if x>0 and y>0:
  print("First coordinate")
elif x<0 and y>0:
  print("Second Coordinate")
elif x<0 and y<0:
  print("Third Coordinate")
elif x>0 and y<0:
  print("Fourth Coordinate")
elif x==0 and y==0:
  print("At origin")
elif x==0 and y>0:
  print("In positive y axis")
elif x==0 and y<0:
  print("In negative y axis")
elif y==0 and x>0:
  print("In positive x axis")
elif y==0 and x<0:
  print("In negative x axis")
else:
  print("Error!")
