#this function is used to determine the equivalent resistance of resistors connected in series
def series(*r):
  return sum(r)
#series(5,4,1) will return a value of 10

#this function is used to determine the equivalent resistance of resistors connected in parallel
def parallel(*r):
  sum = 0
  for i in range(len(r)):
    sum = sum + (1/float(r[i]))
  return (1/sum)
#parallel(2,3) will return a value of 1.2000000000000002
