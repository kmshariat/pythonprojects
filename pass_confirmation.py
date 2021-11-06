# setting new password

previous_password = "prev"
confirm_password = ""
new_password = ""
guess_count = 0
guess_limit = 3
while confirm_password != previous_password and guess_count<guess_limit:
  confirm_password = input("Enter previous Password : ")
  guess_count += 1
  if confirm_password == previous_password:
    new_password = input("Enter your new password")
if guess_count==guess_limit:
  print("back Off")
  
