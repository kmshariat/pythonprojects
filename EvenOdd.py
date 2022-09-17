#this function returns the number of odd terms present in a series
def countOdd(terms):
    count = 0
    for i in range(terms):
        num = int(input('Enter number'))
        if num%2 == 1:
            count += 1
    return count
  
#this function returns the number of even terms present in a series
def countEven(terms):
    count = 0
    for i in range(terms):
        num = int(input('Enter number'))
        if num%2 == 0:
            count += 1
    return count
