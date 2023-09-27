class Player:

  def __init__(self, life, attack, defense, dexterity):
    self.life = life
    self.attack = attack
    self.defense = defense
    self.dexterity = dexterity
    self.inventory = []

  def get_item(self, item):
    self.inventory.append(item)

  def use_item(self, index):
    self.inventory[index].use(self)
