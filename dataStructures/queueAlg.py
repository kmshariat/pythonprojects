#FIFO = First In First Out
def fifo(*arg):
    list_arg = list(arg) 
    for i in range(len(arg)):
        print(list_arg)
        list_arg.pop(0)

#LIFO = Last In First Out
def lifo(*arg):
    list_arg = list(arg) 
    for i in range(len(arg)):
        print(list_arg)
        list_arg.pop(len(arg)-i-1)
