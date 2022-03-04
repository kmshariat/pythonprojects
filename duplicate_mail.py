#This line declares mail ids
mails = ["abc@gmail.com", "def@gmail.com", "abc@gmail.com", "def@gmail.com", "afd@gmail.com"]
#this line creates a dictionary from the list and have keys equal to the list items. This duplicate items are automatically removed 
mails = list(dict.fromkeys(mails)) #We also convert the dictionary into list to get it printed
print(mails)
