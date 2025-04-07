import os
import time
import random

def title_screen():
    """
    Displays the title screen of the Tamagotchi game.
    """
    # Title screen ASCII art

    title_screen_art ="""
    888                                                888           888     d8b 
    888                                                888           888     Y8P 
    888                                                888           888         
    888888 8888b. 88888b.d88b.  8888b.  .d88b.  .d88b. 888888 .d8888b88888b. 888 
    888       "88b888 "888 "88b    "88bd88P"88bd88""88b888   d88P"   888 "88b888 
    888   .d888888888  888  888.d888888888  888888  888888   888     888  888888 
    Y88b. 888  888888  888  888888  888Y88b 888Y88..88PY88b. Y88b.   888  888888 
    "Y888 "Y888888888  888  888"Y888888 "Y88888 "Y88P"  "Y888 "Y8888P888  888888 
                                            888                                  
                                       Y8b d88P                                  
                                        "Y88P"    
    """

    lines = title_screen_art.strip("\n").split("\n")
    width = os.get_terminal_size().columns  # get terminal width
    scroll_range = width + max(len(line) for line in lines)

    for i in range(scroll_range):
        os.system('cls' if os.name == 'nt' else 'clear')
        for line in lines:
            print(line[max(0, i - width):i])
        time.sleep(0.03)


title_screen()
print("Welcome to Tamagotchi!")
print("You have a pet that you need to take care of.")


class Tamagotchi():
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.happiness = 5
        self.health = 5
        self.cleanliness = 5
        self.training = 5
        self.mood = None


    #moods
    def face(self, mood):
        faces = {'happy': '^_^', 'sad': ';_;', 'hungry':':Q', 'angery':'>:[', 'sleepy':'-_- zZ', 'excited':'*^_^*', 'dead':'X_X', 'default':'0~0'}
        if mood in faces:
            return faces[mood]
        else:
            return faces['default']

    #feeding

    #playing

    #cleaning

    #disciplining

    #display
    def display(self):
        print(f" _______________________")
        print(f"|{str(self.name).ljust(23)}|") #left justify name to 23 spaces
        print(f"|{self.face(self.mood).center(23)}|") #center the face in 18 spaces
        print(f"|                       |")
        print(f"|                       |")
        print(f"|Mood: {self.mood.ljust(17)}|")
        print(f"|Hunger: {str(self.hunger).ljust(15)}|")
        print(f"|Happiness: {str(self.happiness).ljust(12)}|")
        print(f"|Health: {str(self.health).ljust(15)}|")
        print(f"|Cleanliness: {str(self.cleanliness).ljust(10)}|")
        print(f"|Training: {str(self.training).ljust(13)}|")
        print(f"|Mood: {str(self.mood).ljust(17)}|")
        print(f"|_______________________|")
        """
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Health: {self.health}")
        print(f"Cleanliness: {self.cleanliness}")
        print(f"Training: {self.training}")
        print(f"Mood: {self.mood}")
        """

pet = Tamagotchi(input("What would you like to name your Tamagotchi pet? :> ")) #instantiate a new pet with name from input



print(pet.face('dead')) #test
print(pet.name) #test

pet.mood = 'hyped'#default as not in faces dict
print(pet.face(pet.mood)) #test

pet.mood = 'sleepy'#sleepy face as it is in dict
print(pet.face(pet.mood)) #test
pet.happiness += 1 #test increase a stat
print(pet.display())
