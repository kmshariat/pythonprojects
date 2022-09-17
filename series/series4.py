#print the series
# 1, 4, 9, 16, 5, 36, 49, ... 
# yes thats 5 not 25

def series(lastNum):
    for i in range(lastNum):
        if i+1 == 5:
            print('5')
        else:
            print((i+1)**2)
