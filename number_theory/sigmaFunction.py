#difining a function called divisor. It is able to find the divisors of a number
def divisor(num):
  num_list= []
  for i in range(num):
	  if num%(i+1)==0:
		  num_list.append(i+1)
  return num_list

#tau function determines the number of divisors
def tau(num):
  return len(divisor(num))

#sigma function determines the sum of divisors
def sigma(num):
  return sum(divisor(num))
    
#getting user input
num = int(input("Enter a number "))

#output
print(f"The divisors are: {divisor(num)}")
print(f"Number of the divisors: {tau(num)}")
print(f"Sum of divisors: {sigma(num)}")
