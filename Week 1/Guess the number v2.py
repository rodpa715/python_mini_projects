import random

def game():
    mysteryNumber = random.randint(1,10)
    print("I just guessed a number.")
    inputByUser = input("Now choose a number from 1 to 10 : ")
    chosenNumber = int(inputByUser)
    
    if chosenNumber == mysteryNumber :
        print("You guessed it right.")
        startingGame()
    elif (chosenNumber > 10) or (chosenNumber < 1):
        print("The number you chose ' {} ' is not a valid number.".format(chosenNumber))
        game()  
    elif chosenNumber < mysteryNumber :
        print("Too low. Try again buddy.")
        game()
    elif chosenNumber > mysteryNumber :
        print("Too high. Try again buddy.")
        game()
   


def startingGame():
    startMenu = input("""Welcome to my guess the number game,
do you want to play? Type YES or NO.""")
    if startMenu == "YES":
        game()
    elif startMenu == "NO":
        print("Thank you for not playing the game. Bye.")
        exit()
    else:
        print("The command you entered ' {} ' is not a valid command.".format(startMenu))
        startingGame()
        
def main():
    startingGame()

if __name__ == '__main__':
    main()

    

    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        
    
    

        

