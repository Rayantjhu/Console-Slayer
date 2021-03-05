class Player():
  def __init__(self, name, health, defense, gear, level, purse, weapon, effect, first_timer, floor_beaten, unlocked_weapons):
    self.name = name
    self.health = health
    self.defense = defense
    self.gear = gear
    self.level = level
    self.purse = purse
    self.weapon = weapon
    self.effect = effect
    self.first_timer = first_timer
    self.floor_beaten = floor_beaten
    self.unlocked_weapons = unlocked_weapons

player = Player(
  name = None,
  health = 100,
  defense = 0,
  gear = None,
  level = 1,
  purse = 0,
  weapon = None, 
  effect = None,
  first_timer = True,
  floor_beaten = None,
  unlocked_weapons = None
)

class Enemy():
  def __init__(self, name, health, defense, damage, level, coin_drop_range):
    self.name = name
    self.health = health
    self.defense = defense
    self.damage = damage
    self.level = level
    self.coin_drop_range = coin_drop_range

class Weapon():
  def __init__(self, name, damage, price, crit_chance, crit_damage, floor):
    self.name = name
    self.damage = damage
    self.price = price
    # crit chance will be in a range of 1-100
    self.crit_chance = crit_chance
    # it will be a multiplier of the base damage. Will be in a range of 0-10
    # 1 = dmg * 1.1; 2 = dmg * 1.2; .. 10 = dmg * 2
    self.crit_damage = crit_damage
    self.floor = floor

class Gear():
  def __init__(self, name, defense, price, floor):
    self.name = name
    self.defense = defense
    self.price = price
    self.floor = floor

class Potion():
  def __init__(self, name, boost, price):
    self.name = name
    self.boost = boost
    self.price = price