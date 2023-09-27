from src.player import Player
import random

class Thalassian(Player):
    def __init__(self,spells=[]):
        self.class_name = "Thalassian"
        self.life = random.randint(15,27)
        self.attack = random.randint(10,18)
        self.defense = random.randint(6,14)
        self.dexterity = random.randint(12, 17)