#this function returns the equivalent capacitance of some capacitors connected in parallel
def parallel(*c):
  return sum(c)
#parallel(0.1,0.2,0.3) will return 0.6

#this function returns the equivalent capacitance of some capacitors connected in series
def series(*c):
  sum = 0
  for i in range(len(c)):
    sum = sum + (1/float(c[i]))
  return (1/sum)
#series(0.1,0.2,0.3) will return 0.05454545454545455
