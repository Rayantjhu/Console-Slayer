from classes import *
import string 
from main_functions import *

def first_time_playing():
  print_and_sleep("Welcome to Console Slayer!", 2)
  print_and_sleep("Before we can start, we are going to need a name.", 2)
  player.name = input("Slayer, what is your name? : ")
  player.first_timer = False
  player.weapon = all_weapons["entrance"]["Fists"]
  time.sleep(1)

  for char in player.name:
    number_name = False
    try:
      if type(int(char)) == int:
        number_name = True
        break
    except ValueError:
      continue

  if len(player.name) > 20 and number_name:
    print_and_sleep("Jesus, that's long..", 2)
    print_and_sleep("And who the fuck puts numbers in their name?", 2)
    print_and_sleep(f"Anyways, welcome to Console Slayer, {player.name}!", 3)
  elif number_name:
    print_and_sleep("Wtf", 1)
    print_and_sleep("Who puts numbers in their name?", 2)
    print_and_sleep(f"Anyways, welcome to Console Slayer, {player.name}!", 3)
  elif len(player.name) > 20:
    print_and_sleep("Jesus, that's long..", 2)
    print_and_sleep(f"Anyways, welcome to Console Slayer, {player.name}!", 3)
  else:
    print_and_sleep(f"Welcome to Console Slayer, {player.name}!", 3)

  print_and_sleep("\nFirst, we're going to have a look at your items.", 3)
  print_and_sleep(f"So far, you've got {player.weapon.name} equipped.", 3)
  print_and_sleep("And yeah, that's not even a weapon, lol.", 2)
  print_and_sleep("Besides, you don't have any gear yet!", 3)
  print_and_sleep("You can always see what gear and weapons you have on you.", 3)
  print_and_sleep("This can be done by typing 'gear' or 'weapon' in the console.", 3)
  
  user_input = input("Go ahead and try it out! : ")
  if user_input.lower() == "gear":
    equipped_gear()
    print_and_sleep("As you can see you do not have any gear equipped.", 2)
    print_and_sleep("Gear can be used to achieve higher defense.", 2)
    print_and_sleep("And it can also give you more HP.", 2)
    user_input = input("Now try the same thing with 'weapon'. : ")

    if user_input.lower() == "weapon":
      equipped_weapon()
      print_and_sleep("Weapons are used to deal damage to your enemies.", 2)
      print_and_sleep("They also can deal critical damage. Which comes with a crit chance.", 2)
      print_and_sleep("These stats of your weapon can be found by typing 'weapon stats' in the console.", 3)
      user_input = input("You can try that aswell. : ")
      
      if user_input.lower() == "weapon stats":
        weapon_stats()

  elif user_input.lower() == "weapon":
    equipped_weapon()

first_time_playing()