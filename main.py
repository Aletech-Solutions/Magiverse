from src.player import Player
from src.item import Item
from src.classes.sorcerer import Sorcerer
import random
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import button_dialog

#Pl = Player(20, 15, 10, 10)
#I1 = Item("Potion",random.randint(1,5),"life", 1)

player = None
types = [("Sorcerer",0), ("Thalassian",1), ("Sapurai",2), ("Ratten",3)]
classes = [Sorcerer]

if not player:
        type_of_player = button_dialog(
    title='Choose your class',
    text='What is your class?',
    buttons= types,
).run()
player = classes[type_of_player]()

print("Your stats:")
print(f" - Class: {player.class_name}")
print(f" - Life: {player.life}")
print(f" - Attack: {player.attack}")
print(f" - Defense: {player.defense}")
print(f" - Dexterity: {player.dexterity}")