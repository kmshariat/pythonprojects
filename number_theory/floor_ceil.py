#defining the floor function
def floor(n):
  return int(n)
#defining the ceiling funtion
def ceil(n):
  return int(n)+1
#getting user input
num = float(input("Enter a number ")) #float is used to convert the string type to float. don't use int. The def functions will do that
print(f"ceil({num}) = {ceil(num)} and floor({num}) = {floor(num)}")
