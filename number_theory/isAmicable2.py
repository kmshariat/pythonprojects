def propdiv(num):
	divisor = []
	for i in range(num-1):
		if num%(i+1)==0:
			divisor.append(i+1)
	return divisor

def amicable(num1, num2):
	if sum(propdiv(num1)) == num2 and sum(propdiv(num2))==num1:
		print(f"{num1} and {num2} are amicable number")
	else:
		print(f"{num1} and {num2} are not an amicable number")
