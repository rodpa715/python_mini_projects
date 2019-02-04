# Pig Latin is a game of alterations played on the English language game.
# To create the Pig Latin form of an English word,
# the initial consonant sound is transposed
# to the end of the word and an ay is affixed
# (Ex.: "banana" would yield anana-bay).
# Read Wikipedia for more information on rules.

vowels = ["a" ,"e" ,"i" ,"o" ,"u" ,"y"]
special = list('[@_!#$%^&*()<>?/\|}{~:]')
acceptRestart = ["YES", "yes", "Yes", "Y"]
refuseRestart = ["NO", "no", "No", "N"]

word = ""

def startingMessage():
    print("----------------------------------")
    print("This is a Pig Latin word generator. Created by Patrick Rodrigues")
    print("You can end this program anytime by entering the '/end' command.")
    print("----------------------------------")
    return


def errorCheck():
    global vowels
    global special
    if word == "/end":
        print("--------------------------------")
        print("Thank you for using my generator")
        print("--------------------------------")
        exit()
    elif (word.isdigit()):
        print("------------------")
        print("Weird flex but ok.")
        print("------------------")
        pigLatin()    
    elif word[0] == "/":
        print("------------------------------------------")
        print("Exit '/end' is the only avaliable command.")
        print("------------------------------------------")
        pigLatin()
    elif any(i in special for i in word):
        print("------------------------------------------")
        print(f"Your entry '{word}' is not a valid word.")
        print("------------------------------------------")
        pigLatin()
    else:
        return

def wordGen():
    global vowels
    if (word[0] in vowels) or (word[0:1] in vowels):
        result = word.replace(" ", "") + "way"
        print("\nThe word '" +  word + "' that you chose became : " + result)
        pigLatin()
    elif word[0] not in vowels and word[1] not in vowels:
        result = word.replace(" ", "")[2:] + word[0:2] + "ay"
        print("\nThe word '" +  word + "' that you chose became : " + result)
        pigLatin()
    elif word[1] in vowels and word[0] not in vowels:
        result = word.replace(" ", "")[1:] + word[0] + "ay"
        print("\nThe word '" +  word + "' that you chose became : " + result)
        pigLatin()
    else:
        return

def pigLatin():
    global word
    word=input("\nType in a word : ")
    if errorCheck():
        errorCheck()
    else:
        wordGen()

        
def main():
    startingMessage()
    pigLatin()


if __name__ == '__main__':
    main()