#this leapyears function take two range of years as input and return the number of leap year present in the range
def leapyears(year1, year2):
    year1 -= 1
    year2 -= 1
    numOfYears = (year2//4 - year1//4) - (year2//100 - year1//100) + (year2//400 - year1//400)
    return numOfYears
