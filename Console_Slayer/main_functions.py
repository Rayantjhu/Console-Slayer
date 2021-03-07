from classes import *
import time 
from items import * 

def help():
  time.sleep(0.5)
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")  
  print("~~   function name   |   functionality                             ~~")
  print("~~  -------------------------------------------------------------  ~~")
  print("~~   weapon          |   shows your equipped weapon                ~~")
  print("~~   gear            |   shows your equipped gear                  ~~")
  print("~~   weapon stats    |   shows the stats of your equipped weapon   ~~")
  print("~~   gear stats      |   shows the stats of your equipped gear     ~~")
  print("~~   edit name       |   edits your user name                      ~~")
  # print("~~   weapon          |   shows your equipped weapon                ~~")
  # print("~~   weapon          |   shows your equipped weapon                ~~")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
  time.sleep(1)

def print_and_sleep(text, seconds):
  print(text)
  time.sleep(seconds)

def equipped_gear():
  time.sleep(0.5)
  print("\n~~~~~~~~~~~~~~~~~~~~~" + "~" * len(str(player.gear)))
  print(f"~~     Gear : {player.gear}     ~~")
  print("~~~~~~~~~~~~~~~~~~~~~" + "~" * len(str(player.gear)))
  print("\n")
  time.sleep(1)

def equipped_weapon():
  time.sleep(0.5)
  print("\n~~~~~~~~~~~~~~~~~~~~~" + "~" * len(str(player.weapon.name)))
  print(f"~~    Weapon : {player.weapon.name}    ~~")
  print("~~~~~~~~~~~~~~~~~~~~~" + "~" * len(str(player.weapon.name)))
  print("\n")
  time.sleep(1)

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
    time.sleep(1)
  elif len(str(player.weapon.name)) < 7:
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"~~    Weapon : {player.weapon.name}     ~~")
    print(f"~~    Damage : {all_weapons[player.weapon.floor][player.weapon.name].damage}     " + " " * (len(str(player.weapon.name))-len(str(player.weapon.damage))) + "~~")
    print(f"~~    crit chance : {all_weapons[player.weapon.floor][player.weapon.name].crit_chance}    " + "~~")
    print(f"~~    crit damage : {all_weapons[player.weapon.floor][player.weapon.name].crit_damage}    " + "~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n")
    time.sleep(1)

def gear_stats():
  time.sleep(0.5)
  if player.gear is None:
    print("\n~~~~~~~~~~~~~~~~~~~~~")
    print("~~   Gear : None   ~~")
    print("~~~~~~~~~~~~~~~~~~~~~")
    print("\n")
    time.sleep(1)
  else:
    print("\n~~~~~~~~~~~~~~~~~~~~" + "~" * len(player.gear.name))
    print(f"~~    Gear : {player.gear.name}     ~~")
    print(f"~~    Defense : {player.gear.defense}" + (" " * len(player.gear.name)) + "~~")
    print("~~~~~~~~~~~~~~~~~~~~" + "~" * len(player.gear.name))
    print("\n")
    time.sleep(1)

def edit_name():
  time.sleep(0.5)
  print_and_sleep("Type your new desired name.", 0.5)
  player.name = input(": ")
  print_and_sleep(f"Your name has succesfully changed to : {player.name}", 0.5)
  time.sleep(1)

