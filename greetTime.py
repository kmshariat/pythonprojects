#Greetings according to Military timings
time = int(input("Enter time (e.g. 1800): "))
if time <=1200:
  print(f"Good Morning. Its {time} hours")
elif time >1200 and time<1700:
  print(f"Good Afternon. Its {time} hours")
elif time >=1700:
  print(f"Good Evening. Its {time} hours")
else:
  print("Error")
