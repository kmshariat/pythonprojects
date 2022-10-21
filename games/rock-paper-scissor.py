import random

#declaring all the choices
choice = ['rock', 'paper', 'scissor']

#getting input from user
user_choice = input('Enter your choice: ').lower()

#getting input from computer
computer_choice = random.choice(choice)

#decision making and result

if user_choice not in choice:
    print('Invalid Input')
elif user_choice == computer_choice:
    print('Its a tie')
elif(
    (user_choice == 'rock' and computer_choice == 'scissor') or (user_choice== 'paper' and computer_choice=='rock') or (user_choice=='scissor' and computer_choice=='paper')
):
    print('You won')
else: 
    print('You lose')
