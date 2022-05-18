from bs4 import BeautifulSoup
import requests
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

def verseOfTheDay():
    page = BeautifulSoup(requests.get("https://www.christianity.com/bible/daily-bible-verse/").content, 'html.parser')
    verse = page.find('blockquote', attrs={'style': 'font-size:21px'}).text
    print(verse)

def menu():
    categories = open("categories.txt", "r")
    print("Welcome to Holy Scripture! What would you like to do?\n1. View a random bible verse\n2. View the Verse of the Day")
    userInput = int(input("Type your choice then click enter: "))
    if userInput == 1:
        clearTerminal()
        print("Which category would you like to pull a verse from?")
        for i in range(1, 5):
            print(str(i) + ".", categories.readline())
        categories.close()
        userInput2 = int(input("Enter a number or press 'Enter' for more categories: "))
        if userInput2 >= 1:
            if userInput2 == 1:
                verseRead("encouragement.txt")
            elif userInput2 == 2:
                verseRead("Scriptures/faith.txt")
            elif userInput2 == 3:
                verseRead("Scriptures/peace.txt")
            elif userInput2 == 4:
                verseRead("Scriptures/love.txt")
        elif userInput2 == "^[":
            quit()
    if userInput == 2:
        clearTerminal()
        verseOfTheDay()

#Main
menu()
