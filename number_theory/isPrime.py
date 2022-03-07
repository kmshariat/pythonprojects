#This code determines a function that can test is a number is prime or not
def isPrime(num):
  if num == 2:
    print(f"{num} is a prime number")
  elif num <2:
    print(f"{num} Not a prime number")
  else:
    for i in range(2,num):
      if num%i==0:
        print(f"{num} is Not a prime number")
        break
      else:
        print(f"{num} is a Prime number")
        break
num = int(input("Enter a number "))
isPrime(num)
