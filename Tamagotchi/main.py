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

    print(title_screen_art)
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console


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
    faces = {'happy': '^_^', 'sad': ';_;', 'hungry':':Q', 'angery':'>:[', 'sleepy':'-_- zZ', 'excited':'*^_^*', 'dead':'X_X'}


    #feeding

    #playing

    #cleaning

    #disciplining


pet = Tamagotchi(input("What would you like to name your Tamagotchi pet?"))



print(pet.faces['dead'])
print(pet.name)
pet.mood = 'happy'
print(pet.faces[pet.mood])