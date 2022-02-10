x = int(input("Enter a number: "))
F = 1
for i in range(x):
  F = F + F*i
print(f"Factorial of x = x! = {F}")
