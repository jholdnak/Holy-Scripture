from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from bs4 import BeautifulSoup
import requests
import random

class HolyScripture(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (.6, .7)
        self.window.pos_hint = {"center_x": .5, "center_y": .5}

        #Logo
        self.window.add_widget(Image(source="logo.png"))
        
        #Label
        self.greeting = Label(text="Welcome! What would you like to do?", font_size = 18, color='#008AD8')
        self.window.add_widget(self.greeting)
        #Buttons
        self.button1 = Button(
                      text="VIEW A RANDOM BIBLE VERSE",
                      size_hint = (1, .5),
                      bold = True,
                      background_color = '#008AD8'
                      )
        self.button2 = Button(
                      text="VIEW THE VERSE OF THE DAY",
                      size_hint = (1, .5),
                      bold = True,
                      background_color = '#008AD8'
                      )
        self.button1.bind(on_press=self.verseRead)
        self.window.add_widget(self.button1)
        self.button2.bind(on_press=self.verseOfTheDay)
        self.window.add_widget(self.button2)

        return self.window

    def verseRead(self, instance):
        categoryFile = open("Scriptures/encouragement.txt", "r")
        verse = categoryFile.readlines()
        randNum = int(random.randint(1, 20))
        categoryFile.close()
        self.greeting.text = verse[randNum]

    def verseOfTheDay(self, instance):
        page = BeautifulSoup(requests.get("https://www.christianity.com/bible/daily-bible-verse/").content, 'html.parser')
        verse = page.find('blockquote', attrs={'style': 'font-size:21px'}).text
        self.greeting.text = verse

if __name__ == "__main__":
    HolyScripture().run()
