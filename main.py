import random
import os

#Functions
def clearTerminal():
    os.system('cls' if os.name=='nt' else 'clear')

def verseRead(category):
    categoryFile = open(category, "r")
    verse = categoryFile.readlines()
    randNum = int(random.randint(1, 20))
    clearTerminal()
    print(verse[randNum])
    categoryFile.close()

def menu():
    categories = open("categories.txt", "r")
    print("Welcome to Holy Scripture! From which category would you like to pull your verse from?")
    for i in range(1, 5):
        print(str(i) + ".", categories.readline())
    categories.close()
    userInput = int(input("Enter a number or press 'Enter' for more categories: "))
    if userInput >= 1:
        if userInput == 1:
            verseRead("Scriptures/encouragement.txt")
        elif userInput == 2:
            verseRead("Scriptures/faith.txt")
        elif userInput == 3:
            verseRead("Scriptures/peace.txt")
        elif userInput == 4:
            verseRead("Scriptures/love.txt")
    else:
        quit()

#Main
menu()
