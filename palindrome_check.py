word = input("Enter a word ")
word = word.lower()
reverse_word = word[::-1]
if word == reverse_word:
  print(f"{word} is a palindrome")
else:
  print(f"{word} is not a palindrome")
