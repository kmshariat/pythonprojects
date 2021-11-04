# A function to determine the maximum between three numbers
def max_num(num1,num2,num3):
  if num1>num2:
    if num1>num3:
      return num1
    else:
      return num3
  elif num2>num3:
      return num2
  else:
      return num3
print(max_num(4,3,6))
