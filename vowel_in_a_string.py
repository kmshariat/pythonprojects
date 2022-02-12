#this code prints the vowels in a string with their positions
word = input("Input a string ")
short_word = word.lower() #this .lower() method is used to lowercase all characters of the string to process easily
n = len(word)
for i in range(n):
	if word[i]=='a' or word[i]=='e' or word[i]== 'i' or word[i] =='o' or word[i]=='u':
		print(f"{i+1}th alphabet is : {word[i]}")
