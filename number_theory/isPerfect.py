#difining a function called divisor. It is able to find the divisors of a number
def divisor(num):
  num_list= []
  for i in range(num):
	  if num%(i+1)==0:
		  num_list.append(i+1)
  return num_list

#defining a function to find the sum of divisors.
def sigma(num):
  return sum(divisor(num))

#getting user input
num = int(input("Enter a number "))

#checking if it is a perfect number or not
if sigma(num)==2*num:
  print("The number is perfect")
else:
  print("Not perfect")
