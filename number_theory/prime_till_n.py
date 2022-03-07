#first defined a function to determine divisors of a number
def divisor(num):
  num_list= []
  for i in range(num):
	  if num%(i+1)==0:
		  num_list.append(i+1)
  return num_list
#Then define a function to determine how many divisors
def tau(num):
  return len(divisor(num))
#Getting user input about the maximum limit of the number
num = int(input("Enter max limit: "))
#Getting the primes
#if a number has only two divisors then thats a prime
for j in range(num):
  if tau(j)==2:
    print(f"{j} is a prime")
