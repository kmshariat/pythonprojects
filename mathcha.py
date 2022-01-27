#creating a mathcha
import random
num1 = random.randint(1,100)
num2 = random.randint(1,100)
ans = num1+num2
user_ans = int(input(f"What is {num1}+{num2}? "))
if ans == user_ans:
  print("passed")
else:
  print("failed")
