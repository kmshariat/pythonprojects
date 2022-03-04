#Voltage divider 
def v_divider(v,r1,r2):
  v1 = float((float(r1)*float(v))/(float(r1)+float(r2)))
  v2 = float((float(r2)*float(v))/(float(r1)+float(r2)))
  print("Voltage across r1: "+str(v1)+" and voltage accross r2: "+str(v2))
v = input("Enter the total voltage: ")
r1 = input("Enter the equvalent resistance r1 : ")
r2 = input("Enter the equivalent resistance r2: ")
v_divider(v,r1,r2)
