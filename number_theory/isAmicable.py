#difining a function called divisor. It is able to find the divisors of a number
def divisor(num):
  num_list= []
  for i in range(num):
	  if num%(i+1)==0:
		  num_list.append(i+1)
  return num_list

#sigma function determines the sum of divisors
def sigma(num):
  return sum(divisor(num))

#getting user input
num1 = int(input("Enter a number "))
num2 = int(input("Enter another number "))

#output
if sigma(num1)==sigma(num2):
  print(f"{num1} and {num2} are amicable")
else:
  print(f"{num1} and {num2} are not amicable")
