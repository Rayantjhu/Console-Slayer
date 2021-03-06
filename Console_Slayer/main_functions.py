from classes import *
import time 
from items import * 

def print_and_sleep(text, seconds):
  print(text)
  time.sleep(seconds)

def equipped_gear():
  time.sleep(0.5)
  print("\n~~~~~~~~~~~~~~~~~~~~~" + "~" * len(str(player.gear)))
  print(f"~~     Gear : {player.gear}     ~~")
  print("~~~~~~~~~~~~~~~~~~~~~" + "~" * len(str(player.gear)))
  print("\n")

def equipped_weapon():
  time.sleep(0.5)
  print("\n~~~~~~~~~~~~~~~~~~~~~" + "~" * len(str(player.weapon.name)))
  print(f"~~    Weapon : {player.weapon.name}    ~~")
  print("~~~~~~~~~~~~~~~~~~~~~" + "~" * len(str(player.weapon.name)))
  print("\n")

def weapon_stats():
  time.sleep(0.5)
  if len(str(player.weapon.name)) > 6: 
    print("\n~~~~~~~~~~~~~~~~~~~~~" + "~" * len(str(player.weapon.name)))
    print(f"~~    Weapon : {player.weapon.name}    ~~")
    print(f"~~    Damage : {all_weapons[player.weapon.floor][player.weapon.name].damage}    " + " " * (len(str(player.weapon.name))-len(str(player.weapon.damage))) + "~~")
    print(f"~~    crit chance : {all_weapons[player.weapon.floor][player.weapon.name].crit_chance}    " + " " * (len(str(player.weapon.name))-len(str(player.weapon.crit_chance))-5) + "~~")
    print(f"~~    crit damage : {all_weapons[player.weapon.floor][player.weapon.name].crit_damage}    " + " " * (len(str(player.weapon.name))-len(str(player.weapon.crit_damage))-5) + "~~")
    print("~~~~~~~~~~~~~~~~~~~~~" + "~" * len(str(player.weapon.name)))
    print("\n")
  elif len(str(player.weapon.name)) < 7:
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"~~    Weapon : {player.weapon.name}     ~~")
    print(f"~~    Damage : {all_weapons[player.weapon.floor][player.weapon.name].damage}     " + " " * (len(str(player.weapon.name))-len(str(player.weapon.damage))) + "~~")
    print(f"~~    crit chance : {all_weapons[player.weapon.floor][player.weapon.name].crit_chance}    " + "~~")
    print(f"~~    crit damage : {all_weapons[player.weapon.floor][player.weapon.name].crit_damage}    " + "~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n")

def gear_stats():
  time.sleep(0.5)
  if player.gear is None:
    print("\n~~~~~~~~~~~~~~~~~~~~~")
    print("~~   Gear : None   ~~")
    print("~~~~~~~~~~~~~~~~~~~~~")
    print("\n")
  else:
    print("\n~~~~~~~~~~~~~~~~~~~~" + "~" * len(player.gear.name))
    print(f"~~    Gear : {player.gear.name}     ~~")
    print(f"~~    Defense : {player.gear.defense}" + (" " * len(player.gear.name)) + "~~")
    print("~~~~~~~~~~~~~~~~~~~~" + "~" * len(player.gear.name))
    print("\n")