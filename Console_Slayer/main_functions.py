from classes import *
import time 
from items import * 

def print_and_sleep(text, seconds):
  print(text)
  time.sleep(seconds)

def equipped_gear():
  time.sleep(0.5)
  print("~~~~~~~~~~~~~~~~~~~~~" + "~" * len(str(player.gear)))
  print(f"~~     Gear : {player.gear}     ~~")
  print("~~~~~~~~~~~~~~~~~~~~~" + "~" * len(str(player.gear)))


def equipped_weapon():
  time.sleep(0.5)
  print("~~~~~~~~~~~~~~~~~~~~~" + "~" * len(str(player.weapon.name)))
  print(f"~~    Weapon : {player.weapon.name}    ~~")
  print("~~~~~~~~~~~~~~~~~~~~~" + "~" * len(str(player.weapon.name)))

def weapon_stats():
  time.sleep(0.5)
  if len(str(player.weapon.name)) > 6: 
    print("~~~~~~~~~~~~~~~~~~~~~" + "~" * len(str(player.weapon.name)))
    print(f"~~    Weapon : {player.weapon.name}    ~~")
    print(f"~~    Damage : {all_weapons[player.weapon.floor][player.weapon.name].damage}    " + " " * (len(str(player.weapon.name))-len(str(player.weapon.damage))) + "~~")
    print(f"~~    crit chance : {all_weapons[player.weapon.floor][player.weapon.name].crit_chance}    " + " " * (len(str(player.weapon.name))-len(str(player.weapon.crit_chance))-5) + "~~")
    print(f"~~    crit damage : {all_weapons[player.weapon.floor][player.weapon.name].crit_damage}    " + " " * (len(str(player.weapon.name))-len(str(player.weapon.crit_damage))-5) + "~~")
    print("~~~~~~~~~~~~~~~~~~~~~" + "~" * len(str(player.weapon.name)))
  elif len(str(player.weapon.name)) < 7:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"~~    Weapon : {player.weapon.name}     ~~")
    print(f"~~    Damage : {all_weapons[player.weapon.floor][player.weapon.name].damage}     " + " " * (len(str(player.weapon.name))-len(str(player.weapon.damage))) + "~~")
    print(f"~~    crit chance : {all_weapons[player.weapon.floor][player.weapon.name].crit_chance}    " + "~~")
    print(f"~~    crit damage : {all_weapons[player.weapon.floor][player.weapon.name].crit_damage}    " + "~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
