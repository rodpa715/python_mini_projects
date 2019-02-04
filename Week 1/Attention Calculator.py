import time
import sys

def welcomeMessage():
    print("Hi this is an attention calculator made for wholesome couples.")
    print("Created by Patrick Rodrigues with bakita in mind.")
    playGame=input("Do you want to play? Type Yes or No : ")
    if (playGame == "YES") or (playGame == "Yes") or (playGame == "yes") or (playGame == "Y") or (playGame == "y"):
        print("\nYou will be asked a series of questions be ready to answer them.")
        progressBar()
        inputData()
    elif (playGame == "NO") or (playGame == "No") or (playGame == "no") or (playGame == "N") or (playGame == "n"):
        print("\nThank you for no playing the game you libtard. Fuck off")
        exit()
    else:
        print("\n###ERROR### \nThe value you entered '{}' is not a valid input.".format(playGame))
        print("###RESTARTING###")
        progressBar()
        welcomeMessage()

def inputData():
    global nameInput, ageInput, heightInput, sexInput, timeTogether
    nameInput = input("\nWhat's your partner's name? : ")
    ageInput = input("\nHow old is your partner? : ") 
    heightInput = input("\nHow tall is your partner in cm? : ")
    timeTogether = input("\nRoughly how many months have you been together? : ")
    sexInput =input("\nType in F for female and M for male : ")
    return nameInput, ageInput, heightInput, sexInput, timeTogether
    
def calculateAttention():
    global nameInput, ageInput, heightInput, attentionTotal, timeTogether
    attentionTotal = int(ageInput) * int(heightInput) * len(nameInput) ** int(timeTogether)

def finalPhrase():
    global nameInput, heightInput, ageInput, attentionTotal, sexInput, timeTogether
    if (sexInput == "M") or (sexInput == "m"):
        print("""\nYour partner's name is {}, he has {}cm of cuteness and is {} years old,
and he has been your loving man for {} months.
Using advanced computation skills, this program has determined that he
deserves exactly {} au/h also known as attention units.
So go get what your man deserves""".format(nameInput, heightInput, ageInput, timeTogether, attentionTotal))
    elif (sexInput == "f") or (sexInput == "F"):
        print("""\nYour partner's name is {}, she has {}cm of cuteness and is {} years old,
and she has been your loving girl for {} months.
Using advanced computation skills, this program has determined that she
deserves exactly {} au/h  also known as attention units.
So go get what your girl deserves!!""".format(nameInput, heightInput, ageInput, timeTogether, attentionTotal))


def progressBar():
    toolbar_width = 50
    
    # setup toolbar
    sys.stdout.write("\n[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
    
    for i in range(toolbar_width):
        time.sleep(0.1) # do real work here
        # update the bar
        sys.stdout.write("-")
        sys.stdout.flush()
    
    sys.stdout.write("\n")
    
def restartMessage():
    print("\nDo you wish to reset the calculator?")
    resetInput=input("\nType Yes if you want to reset.\nType No if you want to exit the program : ")
    if (resetInput == "YES") or (resetInput == "Yes") or (resetInput == "yes") or (resetInput == "Y") or (resetInput == "y"):
        print("\nProgram will be restarted")
        progressBar()
        welcomeMessage()
    elif (resetInput == "NO") or (resetInput == "No") or (resetInput == "no") or (resetInput == "N") or (resetInput == "n"):
        print("\nThank you for  playing the game you cutiepie.")
        exit()
    else:
        print("\n###ERROR### \nThe value you entered '{}' is not a valid input.".format(resetInput))
        print("###RESTARTING###")
        progressBar()
        welcomeMessage()   

welcomeMessage()
calculateAttention()
progressBar()
finalPhrase()
restartMessage()




