#a code to print fibonacci sequence
term1 = 1
term2 = 1
next_term = term1+term2
n = int(input("Enter how many terms you want: "))
print(term1)
print(term2)
for i in range(n-2):
  print(next_term)
  term1 = term2
  term2 = next_term 
  next_term = term1+term2
