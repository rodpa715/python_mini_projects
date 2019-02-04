import random

mysteryNumber = random.randint(1,10)
print("I just guessed a number.")

inputByUser = input("Now choose a number from 1 to 10 : ")
chosenNumber = int(inputByUser)
    
if mysteryNumber == chosenNumber:
    print("You guessed it right.")
elif mysteryNumber > chosenNumber:
    print("Too low. Try again buddy.")
elif mysteryNumber < chosenNumber:
    print("Too high. Try again buddy.")
