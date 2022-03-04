import random
chars = [0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","$","%","&","*","_"]
mail = ""
for i in range(5):
  random_chars = random.choice(chars)
  mail = mail + str(random_chars)
print(f"{mail}@gmail.com is a randomly generated e-mail ") 
