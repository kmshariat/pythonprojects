# Write a function that prints the numbers from 1 to num_range 
# and for multiples of ‘3’ print “Fizz” instead of the number 
# and for the multiples of ‘5’ print “Buzz”. 
# and if it is divisible by both '3' and '5' then print "Fizzbuzz"

def fizzbuzz(num_range):
    for num in range(num_range+1):
        if num % 3 ==0 and num % 5 ==0:
            print('FizzBuzz')
            continue
        elif num % 3 ==0:
            print('Fizz')
            continue
        elif num % 5 ==0:
            print('Buzz')
            continue
        print(num)
