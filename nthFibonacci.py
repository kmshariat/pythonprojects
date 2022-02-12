#a code to print nth fibonacci sequence number
term1 = 1
term2 = 1
next_term = term1+term2
n = int(input("Enter how many terms you want: "))
for i in range(n-3):
  term1 = term2
  term2 = next_term 
  next_term = term1+term2
print(f"{n}th term is {next_term}")
