#Better Calculator
num1 = float(input("Enter first number: "))
print("----------")
print("Directions")
print("----------")
print("Enter Operator + to add, - to subtract, * to multiply and / to divide")
op = input("Enter Operator: ")
num2 = float(input("Enter another number: "))
if op == "+":
  print(num1+num2)
elif op == "-":
  print(num1-num2)
elif op == "*":
  print(num1*num2)
elif op == "/":
  print(num1/num2)
else:
  print("Invalid Operator")
