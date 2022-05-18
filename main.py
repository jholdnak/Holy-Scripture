import random
import os

def clearTerminal():
    os.system('cls' if os.name=='nt' else 'clear')

def verseRead(category):
    categoryFile = open(category, "r")
    verse = categoryFile.readlines()
    randNum = int(random.randint(1, 25))
    clearTerminal()
    print(verse[randNum])
    categoryFile.close()

def menu():
    categories = open("/home/joseph/Filen Sync/Coding/SideProjects/Holy-Scripture/categories.txt", "r")
    print("Welcome to Holy Scripture! From which category would you like to pull your verse from?")
    for i in range(1, 5):
        print(str(i) + ".", categories.readline())
    categories.close()
    userInput = int(input("Enter a number or press 'Enter' for more categories: "))
    if userInput == 1:
        verseRead("/home/joseph/Filen Sync/Coding/SideProjects/Holy-Scripture/Scriptures/encouragement.txt")

menu()