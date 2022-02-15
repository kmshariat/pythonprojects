#function to calculate simple interest
def simpleInterest(p,n,r):
  return p*n*r/100
#function to calculate compound interest
def compoundInterest(p,n,r):
  return p*(1+r/100)**n-p
#getting user inpput
p = float(input("Input your amount: "))
n = float(input("Enter year: "))
r = float(input("Enter interest rate (e.g. 5): "))
#output
print(f"Your simple interest after {int(n)} years will be {simpleInterest(p,n,r)} and total will be {simpleInterest(p,n,r)+p}")
print(f"Your compound interest after {int(n)} years will be {compoundInterest(p,n,r)} and total will be {compoundInterest(p,n,r)+p}")
