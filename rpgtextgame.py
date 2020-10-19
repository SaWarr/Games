# RPG text-based game

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

##### Player setup #####
class PLAYER:
    # Of the class player, we're defining a function that initialises it as itself 
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'start  '
        # Empty placeholders for now, name, health points, mana points, status effects. 
        # Location added

myPlayer = PLAYER()

##### Title Screen #####
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game() # Placeholder until written
    elif option.lower() == ("help"):
        help_menu() # Another placeholder
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play','help','quit']:
        print("Please enter a valid command")
        # Not sure the following needs to be here but following tutorial for now
        option = input("> ")
        if option.lower() == ("play"):
            start_game() # Placeholder until written
        elif option.lower() == ("help"):
            help_menu() # Another placeholder
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')  
    print('###########################')
    print('# Welcome to the text RPG #')
    print('###########################')
    print('    Play, help or quit?    ')
    title_screen_selections()

def help_menu():
    print('#################################')
    print('#### Welcome to the text RPG ####')
    print('Use up, down, left, right to move')
    print('Use "look" to inspect something')    
    print('Type your commands to enact them')
    print('#    Good luck and have fun!    #')
    title_screen_selections()

def start_game(): 
