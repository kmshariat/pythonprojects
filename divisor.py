#difining a function called divisor. It is able to find the divisors of a number
def divisor(num):
    for i in range(num):
	    if num%(i+1)==0:
		    print(f"{i+1} is a divisor of  {num}")
#getting user input
num = int(input("Enter a number "))
divisor(num)
