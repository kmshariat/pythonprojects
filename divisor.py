#difining a function called divisor. It is able to find the divisors of a number
def divisor(num):
	divisor = []
	for i in range(num):
		if num%(i+1)==0:
			divisor.append(i+1)
	return divisor
