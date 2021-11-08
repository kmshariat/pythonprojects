#Exponent Function
def exp(base,power):
  result = 1
  for index in range(power):
    result = result*base
  return result 

base = int(input("Enter base: ")) 
power = int(input("Enter power: "))
exp(base,power)
