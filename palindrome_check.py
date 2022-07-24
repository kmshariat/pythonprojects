def palindrome(word):
    word = str(word).lower()
    reverse_word = word[::-1]
    if word == reverse_word:
      print(f"{word} is a palindrome")
    else:
      print(f"{word} is not a palindrome")
      
#test_case 1: palindrome('MOM') -> mom is a palindrome
#test_case 2: palindrome('wizard') -> wizard is not a palindrome
#test_case 3: palindrome(3829) -> 3829 is not a palindrome
