def divisor(num):
  num_list= []
  for i in range(num):
	  if num%(i+1)==0:
		  num_list.append(i+1)
  return num_list
num = int(input("Enter a number to check: "))
if len(divisor(num))==2:
  print(f"{num} is a prime")
else:
  print(f"{num} is not a prime")
