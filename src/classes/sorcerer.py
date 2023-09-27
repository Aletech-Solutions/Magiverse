from src.player import Player
import random

class Sorcerer(Player):
    def __init__(self,spells=[]):
        self.class_name = "Sorcerer"
        self.life = random.randint(15,25)
        self.attack = random.randint(5,12)
        self.defense = random.randint(10,18)
        self.dexterity = random.randint(10, 15)