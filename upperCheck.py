#this takes a string and stores the value in word variable
word = input("Enter a word: ")

#defining a function called checkWord() which will check if the given word's first letter is upper case or not
def checkWord(word):
  if word[0] == word[0].upper():    
    print("True")
  else: 
    print("False") 

#calling the function
checkWord(word)
