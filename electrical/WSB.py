#Wheatstone Bridge
#For the circuit you can see this wikipedia file https://en.wikipedia.org/wiki/Wheatstone_bridge#/media/File:Wheatstonebridge_current.svg 
def WSB(r1,r2,r3,r4):
  if ((r1/r3)==(r2/r4)):
    print("The bridge is in equilibrium position")
  else: 
    x  = r3*(r2/r1) - r4
    print("Add "+str(x)+" ohm resistance in series with r4 to make it in equilibrium")
r1 = float(input("Enter the resistance at the first arm r1: "))
r2 = float(input("Enter the resistance at the second arm r2: "))
r3 = float(input("Enter the resistance at the third arm r3: "))
r4 = float(input("Enter the resistance at the fourth arm r4: "))
WSB(r1,r2,r3,r4)
