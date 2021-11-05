#Password Confirm

password = "previous_pass"
confirm_password = ""
while confirm_password != password :
  confirm_password = input("Enter Your Previous Password: ")
password = input("Enter new password : ")
print("your new password is "+password)
