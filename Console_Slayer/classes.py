class Player():
  def __init__(self, name, health, defense, damage, level, purse, weapon, effect, backpack):
    self.name = name
    self.health = health
    self.defense = defense
    self.damage = damage
    self.level = level
    self.purse = purse
    self.weapon = weapon
    self.effect = effect
    self.backpack = backpack

class Enemy():
  def __init__(self, name, health, defense, damage, level, coin_drop_range):
    self.name = name
    self.health = health
    self.defense = defense
    self.damage = damage
    self.level = level
    self.coin_drop_range = coin_drop_range

class Weapon():
  def __init__(self, name, damage, price):
    self.name = name
    self.damage = damage
    self.price = price


class Armor():
  def __init__(self, name, defense, price):
    self.name = name
    self.defense = defense
    self.price = price

class Potion():
  def __init__(self, name, boost, price):
    self.name = name
    self.boost = boost
    self.price = price