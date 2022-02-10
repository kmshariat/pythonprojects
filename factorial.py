x = int(input("Enter a number: "))
if x>0:
  F = 1
  for i in range(x):
    F = F + F*i
  print(f"Factorial of x = x! = {F}")
else:
  print("Not in range")
