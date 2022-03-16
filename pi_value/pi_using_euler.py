#determinating pi using Euler's convergence improvement transformation (Beeler et al. 1972, Item 120)
d = 1
sum = 0
for i in range(1000):
	d = (d*(i+1))/(2*i+1)
	sum = sum + d
print(f"pi is: {2*sum-2}")
