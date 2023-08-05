import random

# a function to generate random password of 8 characters
def randpass():
    chars = [0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","$","%","&","*","_"]
    password = ""

    for i in range(8):
        random_chars = random.choice(chars)
        password = password +str(random_chars)
    return print(password)

#testing
if __name__ == "__main__":
    randpass()
