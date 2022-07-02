#this function will take two inputs the number that I want to print and the row number about how many rows I want to print. 
def pattern_same(num,row):
  for i in range(row):
    print(str(num)*(i+1))
#pattern_same(2,3) will return
#2
#22
#222

#this function will take the number of rows. It will print number i in the i th row
def pattern_diff(row):
  for i in range(row):
    print(str((i+1))*(i+1))
#pattern_diff(3) will return 
#1
#22
#333 

#this function will take the number of rows. It will print * symbol upto row number as a pyramid structure.
def pyramid(row):
  for i in range(row+1):
    print(" "*(row-i)+" *"*i) #the spaces will create a uniformly distributed pyramid
#pyramid(3) will return
# *
# **
# ***

#this function will take the number of rows. It will print * symbol upto row number as an upside down pyramid structure.
def revPyramid(row):
  for i in range(row+1):
    print(" "*(i+1)+" *"*(row-i))
#revPyramid(3) will return
# ***
# **
# *
