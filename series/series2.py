#1+3+5+ ...
#this code will return the sum of the series where n is the last number

sum = 0 
n = int(input("Enter the value of n: "))
for i in range(1,n,2):
    sum = sum+i
print(sum)
