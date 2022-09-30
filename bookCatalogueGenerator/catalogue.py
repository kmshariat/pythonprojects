#open a file in the reading mode
file = open("books.txt", "r")
array = file.readlines()

n = len(array) 

#generating codes with the first letter of the book's title and the number of characters in the title Such as I22.
for i in range(n):
    print(array[i][0]+ str(len(array[i])-1))

file.close()
