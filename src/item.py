class Item:

  def __init__(self, name, value, affects, rarity):
    self.name = name
    self.value = value
    self.affects = affects
    self.rarity = rarity

  def use(self, player):
    player[self.affects] += self.value
