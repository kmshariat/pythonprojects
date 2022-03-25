# [Ref: Braun, C. (1893). A Simple Rule for finding the Day of the Week corre spondingtoanygiven Day of the Month and Year. Nature, 48(1236), 222-223.]
#there are still bugs. The 21st century dates are one day behind and 20th century get the months wrong and still have to add condition about leap year

month = input("Enter month name: ").lower()
day = int(input("Enter day of the month: "))
if day > 31:
  print("Invalid day of the month")
year = int(input("Enter year: "))

#month codes
if year >= 2000 and year < 3000:
  if month == "january":  
    month = 8
  elif month == "february":
    month = 11
  elif month == "march": 
    month = 11
  elif month == "april":
    month = 7
  elif month == "may":
    month = 12
  elif month =="june":
    month = 5
  elif month == "july":
    month = 7
  elif month=="august":
    month = 8
  elif month=="september":
    month = 6  
  elif month=="october":
    month = 18
  elif month=="november": 
    month = 11
  elif month=="december":
    month = 6


elif year >= 1900 and year < 2000:
  if month == "january":  
    month = 3
  elif month == "february":
    month = 6
  elif month == "march": 
    month = 6
  elif month == "april":
    month = 2
  elif month == "may":
    month = 5
  elif month =="june":
    month = 0
  elif month == "july":
    month = 2
  elif month=="august":
    month = 3
  elif month=="september":
    month = 1  
  elif month=="october":
    month = 3
  elif month=="november": #there is a bug here
    month = 6
  elif month=="december":
    month = 1
else:
  print("Out of year range")
year = str(year)[2:4]
year = int(year)
print(f"Sequence: {day} : {month} : {year} : {int(year/4)}")
remain = (day+month+year+int(year/4))%7
if remain == 1:
  print("It was sunday")
elif remain == 2:
  print("It was monday")
elif remain == 3:
  print("It was tuesday")
elif remain == 4:
  print("It was wednesday")
elif remain == 5:
  print("It was thursday")
elif remain== 6:
  print("It was friday")
elif remain == 0:
  print("It was saturday")
