#Current divider
def i_divider(i,r1,r2):
  i1 = float((float(r2)*float(i))/(float(r1)+float(r2)))
  i2 = float((float(r1)*float(i))/(float(r1)+float(r2)))
  print("Current through r1: "+str(i1)+" and curent through r2: "+str(i2))
i = input("Enter the total current: ")
r1 = input("Enter the equivalent resistance r1 : ")
r2 = input("Enter the equivalent resistance r2 : ")
i_divider(i,r1,r2)
