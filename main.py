from src.player import Player
from src.item import Item
from src.classes.sorcerer import Sorcerer
from src.classes.thalassian import Thalassian

import random
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import button_dialog, input_dialog
from prompt_toolkit import print_formatted_text, HTML
from src.utils import print_attributes

from prompt_toolkit import prompt
import inquirer


player = None
name = None

classes = [Sorcerer,Thalassian]
types = [("Sorcerer",0), ("Thalassian",1), ("Sapurai",2), ("Ratten",3)]
type_choices = [t[0] for t in types]

if not name:
    print_formatted_text(HTML(f'<ansicyan>[Type your name]:</ansicyan>'))
    name = input()

if not player:
    questions = [
        inquirer.List("character_type", message="Select your character type:", choices=type_choices)
    ]
    answers = inquirer.prompt(questions)
    selected_type = answers["character_type"]
    for t in types:
        if selected_type == t[0]:
            print(f"You selected: {t[0]} (ID: {t[1]})")
            player = classes[t[1]]()

print_formatted_text(HTML(f'<ansicyan>Your name: </ansicyan>{name}<br/>'))
print_attributes(player)
print_formatted_text(HTML(f'<ansicyan>[Enter]: </ansicyan>To continue<br/>'))

