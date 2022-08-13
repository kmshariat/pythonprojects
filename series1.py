#1 + (1+2) + (1+2+3) + ...
#the sums in brackkets are declared as partial sum

partial_sum = 0
arr_partial_sum = [] #this array will store the values of each partial sum. we will then add all the values of this array

n = int(input("Enter the value of n: "))

for j in range(n+1):
    partial_sum = partial_sum + j
    arr_partial_sum.append(partial_sum) 

total_sum = sum(arr_partial_sum)
print(total_sum)
