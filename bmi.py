#this program is used to calculate BMI index. Don't know about BMI? Read this: https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html 
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meter: "))
bmi = weight/(height*height)
if bmi>0 and bmi <= 18.5:
  print(f"Your BMI is {bmi}, indicating your weight is in the Underweight category for adults of your height.")
elif bmi >18.5 and bmi <=24.9:
  print(f"Your BMI is {bmi}, indicating your weight is in the Healthy category for adults of your height.")
elif bmi >24.9 and bmi <=29.9:
  print(f"Your BMI is {bmi}, indicating your weight is in the Overweight category for adults of your height.")
elif bmi >29.9:
  print(f"Your BMI is {bmi}, indicating your weight is in the Obese category for adults of your height.")
else:
  print("Error!")
