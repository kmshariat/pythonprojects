# leapYear function tests if a year is a leap year or not
def leapYear(year):
  if year%400==0:
    print(str(year)+" is a leap year")
  elif year%4==0 and year%100!=0:
    print(str(year)+" is a leap year")
  else:
    print(str(year)+ " is not a leap year")

year=int(input("Enter a year: "))
leapYear(year)
