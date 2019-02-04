# make list with consonants [a, e, i, o, u]
# user inputs word
# if the second letter of the word that the user input is a consonat
# 	then the first letter is added to the end of the word + ay
# else
# 	user get's told that the word he inputed is not valid
acceptRestart=["YES", "yes", "Yes", "Y"]
refuseRestart=["NO", "no", "No", "N"]

vowels=["a" ,"e" ,"i" ,"o" ,"u" ,"y"]

word = ""

def startingMessage():
    print("----------------------------------")
    print("This is a Pig Latin word generator")
    print("You can end this program anytime by entering the '/end' command.")
    print("----------------------------------")
    return

def pigLatin():
    global word
    word=input("\nType in a word : ")
    if word == "/end":
        print("--------------------------------")
        print("Thank you for using my generator")
        print("--------------------------------")
        exit()
    elif "/" in word[:]:
        print("------------------------------------------")
        print("Exit '/end' is the only avaliable command.")
        print("------------------------------------------")
        pigLatin()
    elif (word.isdigit()):
        print("------------------")
        print("Weird flex but ok.")
        print("------------------")
        pigLatin()  
    elif (word[0] in vowels) or (word[0:1] in vowels):
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
        
def main():
    startingMessage()
    pigLatin()


if __name__ == '__main__':
    main()