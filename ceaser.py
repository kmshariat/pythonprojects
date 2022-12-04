def Ceaser(userInput,shift):
    plainText = list(userInput)
    cipherText = "" 
    for i in range(len(plainText)):
        cipherText += chr(ord(plainText[i])+shift)
    return cipherText

print(Ceaser("attackatonce",4))  
#output exxegoexsrgi
