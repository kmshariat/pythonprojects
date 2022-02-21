#A program to find the values of pi. [Not 100% accurate as we use iteration limit]
sum = 0
for i in range(10000):
    sum = sum + ((-1)**i)/(2*i+1)
print(4*sum)
