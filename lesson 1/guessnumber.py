print("Welcome to the guess number game")
print("Program picking number...")
import random
a = random.randint(0, 10)

b = int (input("Please input a number within the range of 1 to 10."))
while True:
    if b > a:
        print("The number is too high!")
        b = int (input("Please input a number within the range of 1 to 10."))
    elif  b < a:
        print("The number is too low!")
        b = int (input("Please input a number within the range of 1 to 10."))    
    else:
        break
print("Correct! Game over.")