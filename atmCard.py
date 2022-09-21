"""
Using an ATM, customers can access their bank deposits or 
credit accounts to do a variety of financial transactions.
You serve ATMs that accept only Visa and Amex bank cards.
The given program takes the type of a bank card as input.

Task

Complete the program to output "accepted" if the card is Visa or Amex. Else print "rejected"
"""

type = input("Insert your credit card: ").lower()

if type == 'visa' or type == 'amex':
    print('accepted')
else:
    print("rejected")
