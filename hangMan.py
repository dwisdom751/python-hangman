import sys
import random


if __name__ == "__main__":
    wordsFileName = ""
    
    if(len(sys.argv) < 2):
        print("input the name of the file to get words from")
        wordsFileName = input()
    else:
        wordsFileName = sys.argv[1]
    
    wordsFile = open(wordsFileName, "r").read()
    
    wordsWDup = wordsFile.replace('\n'," ").lower().split(" ")
    
    words = []
    
    #make sure there are no duplicate words
    for word in wordsWDup:
        if word not in words:
            words.append(word)
    
    hidWord = random.choice(words)
    revealedWord = len(hidWord) * "*"
    
    damage = 0
    
    exit = 0
    
    #different asscii art guys to print at different stages of health
    hangGuy = ["","--\n |","--\n |\n O","--\n |\n O\n |","--\n |\n O\n/|","--\n |\n O\n/|\\ ","--\n |\n O\n/|\\\n/","--\n |\n O\n/|\\\n/ \\\n"]
    print(hangGuy[0])
    while(damage <= 6 and exit != 1):
        print(hangGuy[damage])
        print(damage)
        print("revealed word: " + revealedWord + "\n")
        letter = ""
        while letter == "":
            letter = input("input a character(only the first character will be used) or input exit to quit\n")
        if(letter == "exit"):
            exit = 1
        else:
            letter = letter[0]
            if(letter in hidWord):
                for count in range(0,len(hidWord)):
                    if(hidWord[count] == letter):
                        revealedWord = list(revealedWord)
                        revealedWord[count] = hidWord[count]
                        revealedWord = "".join(revealedWord)
            else:
                damage += 1
        
        if(revealedWord == hidWord):
            print("Good Job! You Won! Word was: " + revealedWord)
            exit = 1
    
    if(revealedWord != hidWord):
        print(hangGuy[damage])
        print("sadly you lost :(")
        print("word was " + hidWord)