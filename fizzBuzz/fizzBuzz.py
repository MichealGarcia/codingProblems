# Create solution for fizzbuzz problem

# Define funciton fizzBuzz that takes no parameters
# this solution will print numbers 1 through 100 
# numbers divisible by 3 will print Fizz, 5 Buzz
# and if divisible by 3 and 5 (15) then FizzBuzz

def fizzBuzz():
    # iterate range 1 through 100
    for num in range(1,101):
        # if num in range is divisible by 3 and 5 with a remainder of 0, FizzBuzz
        # We put this first in consideration of computers line by line structure
        if num % 15 == 0:
            print("FizzBuzz")
        # else if num divisible by 3 with remainder 0, Fizz
        elif num % 3 == 0:
            print("Fizz")
        # else if num divisible by 5 with remainder 0, Buzz
        elif num % 5 == 0:
            print("Buzz")
        # else, print the number
        else:
            print(num)
fizzBuzz()


    

