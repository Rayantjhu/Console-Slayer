from classes import *

# name, damage, price, crit_chance, crit_damage
all_weapons = {
  "entrance" : {
    "Fists" : Weapon("Fists", 0, 0, 0, 0, "entrance" ),
    "Brass Knuckles" : Weapon("Brass Knuckles", 1, 10, 1, 1, "entrance"),
    "Rusty Sword" : Weapon("Rusty Sword", 1, 20, 5, 5,"entrance"),
    "Rookie Pistol" : Weapon("Rookie Pistol", 2, 25, 10, 3, "entrance") 
  },
  "tutorial" : {
    "Cleaver" : Weapon("Cleaver", 5, 50, 10, 1, "tutorial"), 
    "Boomerang Gun" : Weapon("Boomerang Gun", 10, 100, 25, 1, "tutorial")
  },
  "floor1" : {
    "Slayer Knuckles" : Weapon("Slayer Knuckles", 25, 350, 20, 6, "floor1" ),
    "Beginner Pistol" : Weapon("Beginner Pistol", 35, 350, 5, 1, "floor1" )
  }
}

all_gear = {
  "entrance" : {
    "Rookie Hoodie" : Gear("Rookie Hoodie", 10, 5, "entrance"),
    "Damaged Helmet" : Gear("Damaged Helmet", 15, 15, "entrance")
  }
}