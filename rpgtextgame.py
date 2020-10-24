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

#### MAP #### 
    """
    Player starts at b2
    a1 a2 a3 a4 
    -------------
    |  |  |  |  | a4
    -------------
    |  |  |  |  | b4...
    -------------
    |  |  |  |  |
    -------------
    |  |  |  |  |
    -------------
    """

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'info'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False,'a4': False,
                'b1': False, 'b2': False, 'b3': False,'b4': False,
                'c1': False, 'c2': False, 'c3': False,'c4': False,
                'd1': False, 'd2': False, 'd3': False,'d4': False,
                }

zone_map = {
    'a1': {
        ZONENAME: "Jungle",
        DESCRIPTION: 'You are surrounded by a lush jungle.',
        EXAMINATION: 'info',
        SOLVED: False,
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2',
    },
    'a2': {
        ZONENAME: "Beach",
        DESCRIPTION: 'You are standing on a golden beach.',
        EXAMINATION: 'info',
        SOLVED: False,
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
    },
    'a3': {
        ZONENAME: "Docks",
        DESCRIPTION: 'You stand on a dock surrounded by a refreshing sea breeze.',
        EXAMINATION: 'info',
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
    },
    'a4': {
        ZONENAME: "Inn",
        DESCRIPTION: '',
        EXAMINATION: 'info',
        SOLVED: False,
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: '',
    },
    'b1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'info',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2',
    },
    'b2': {
        ZONENAME: 'Your room',
        DESCRIPTION: 'This is your bedroom!',
        EXAMINATION: 'Where your walls used to stand there is greyness, a void. It does not seem harmful.',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'b3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'info',
        SOLVED: False,
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4',
    },
    'b4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'info',
        SOLVED: False,
        UP: 'a4',
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: '',
    },
    'c1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'info',
        SOLVED: False,
        UP: 'b1',
        DOWN: 'd1',
        LEFT: '',
        RIGHT: 'c2',
    },
    'c2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'info',
        SOLVED: False,
        UP: 'b2',
        DOWN: 'd2',
        LEFT: 'c1',
        RIGHT: 'c3',
    },
    'c3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'info',
        SOLVED: False,
        UP: 'b3',
        DOWN: 'd3',
        LEFT: 'c2',
        RIGHT: 'c4',
    },
    'c4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'info',
        SOLVED: False,
        UP: 'b4',
        DOWN: 'd4',
        LEFT: 'c3',
        RIGHT: '',
    },
    'd1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'info',
        SOLVED: False,
        UP: 'c1',
        DOWN: '',
        LEFT: '',
        RIGHT: 'd2',
    },
    'd2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'info',
        SOLVED: False,
        UP: 'c2',
        DOWN: '',
        LEFT: 'd1',
        RIGHT: 'd3',
    },
    'd3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'info',
        SOLVED: False,
        UP: 'c3',
        DOWN: '',
        LEFT: 'd2',
        RIGHT: 'd4',
    },
    'd4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'info',
        SOLVED: False,
        UP: 'c4',
        DOWN: '',
        LEFT: 'd3',
        RIGHT: '',
    },
}

#### GAME INTERACTIVITY ####




#### GAME FUNCTIONALITY ####
