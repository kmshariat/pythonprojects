from random import randint

number = randint(0,100)
guesses = 0

while guesses <3:
  
  guesses +=1
  print("--------------------")
  print(f"Guess No. {guesses}")
  usernum = input("Guess a number from 0 to 100: ")

  if int(usernum)==number:
    print(f"You won! {number} is the right guess")
    break

  elif int(usernum) > number:
    print("Guess a lower number ")
    continue

  elif int(usernum) < number:
    print("Guess a higher number ")
    continue

while guesses>=3:
    print('Game Over')
    print("--------------------")
    break
