# A code to determine the value of nPr and nCr
def factorial(x):
  F = 1
  for i in range(x):
    F = F+ F*i
  return F

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

nCr = factorial(n)/(factorial(r)*factorial(n-r))
nPr = factorial(r)*nCr
print(f"The value of nCr:{nCr} and the value of nPr: {nPr}")
