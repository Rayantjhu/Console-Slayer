from classes import *
import string 
from main_functions import *

def first_time_playing():
  # Welome
  print_and_sleep("Welcome to Console Slayer!", 2)
  print_and_sleep("Before we can start, we are going to need a name.", 2)
  
  player.name = input("Slayer, what is your name? : ")
  player.first_timer = False
  player.weapon = all_weapons["entrance"]["Fists"]
  player.available_weapons = [all_weapons["entrance"]["Fists"]]
  player.floor_beaten = ["entrance"]
  
  time.sleep(0.5)

  # Digit check
  for char in player.name:
    number_name = False
    try:
      if type(int(char)) == int:
        number_name = True
        break
    except ValueError:
      continue

  # Name / greeting
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

  # Tutorial Start
  print_and_sleep("\nFirst, we're going to have to take a look at your items.", 3)
  print_and_sleep(f"For now you've got {player.weapon.name} equipped as your weapon.", 3)
  print_and_sleep("And yeah, that's not even a weapon, lol.", 2)
  print_and_sleep("Besides, you don't have any gear yet!", 3)
  print_and_sleep("You can always see what gear and what weapons you have equipped.", 4)
  print_and_sleep("This can be done by typing 'gear' or 'weapon' in the console.", 3)
  
  user_input = input("Go ahead and try it out! : ")

  # Calls Tutorial
  stop = False
  while not stop:
    if user_input.lower() == "gear":
      gear_tutorial()
      stop = True
    elif user_input.lower() == "weapon":
      weapon_tutorial()
      stop = True
    else:
      print_and_sleep("Uhm..", 1)
      print_and_sleep("That's not a what I asked.", 2)
      user_input = input("Please try again. : ")
      continue

def gear_explanation():
  print_and_sleep("As you can see you do not have any gear equipped.", 2)
  print_and_sleep("Gear can be used to achieve higher defense.", 2)
  print_and_sleep("And it can also give you more HP.", 2)

def weapon_explanation():
  print_and_sleep("Weapons are used to deal damage to your enemies.", 2)
  print_and_sleep("They also can deal critical damage. Which comes with a crit chance.", 2)

def gear_tutorial():
  equipped_gear()
  gear_explanation()
  stop = False
  user_input = input("Now try the same thing with 'weapon'. : ")
  while not stop:
    if user_input.lower() == "weapon":
      equipped_weapon()
      weapon_explanation()
      print_and_sleep("These stats of your weapon can be found by typing 'weapon stats' in the console.", 3)
      user_input = input("You can try that aswell. : ")
      stop = True
      stop2 = False
      while not stop2:
        if user_input.lower() == "weapon stats":
          weapon_stats()
          print_and_sleep("Same goes for 'gear stats'.", 2)
          stop2 = True
          stop = True
          print_and_sleep("If you wish to try that you may.", 1)
          print_and_sleep("If you wish to continue. Type 'continue'.", 1)
          user_input = input(": ")
          stop3 = False
          while not stop3:
            if user_input.lower() == "continue":
              stop3 = True
              continue
            elif user_input.lower() == "gear stats":
              gear_stats()
              stop3 = True
              continue
            else:
              print_and_sleep("That's not the correct input!", 2)
              user_input = input("Please try again. : ")
              continue
        else:
          print_and_sleep("That's not the correct input!", 2)
          user_input = input("Please try again. : ")
    else:
      print_and_sleep("That's not the correct input!", 2)
      user_input = input("Please try again. : ")
      continue

def weapon_tutorial():
  equipped_weapon()
  weapon_explanation()
  stop = False
  user_input = input("Now try the same thing with 'gear'. : ")
  while not stop:
    if user_input.lower() == "gear":
      equipped_gear()
      gear_explanation()
      print_and_sleep("You can see the stats of your gear by typing 'gear stats' in the console.", 2)
      user_input = input("You can try that aswell. : ")
      stop2 = False
      stop = True
      while not stop2:
        if user_input.lower() == "gear stats":
          gear_stats()
          print_and_sleep("Same thing can be done for your weapons by typing 'weapon stats'.", 2)

          print_and_sleep("If you wish to try that you may.", 1)
          print_and_sleep("If you wish to continue. Type 'continue'.", 1)
          user_input = input(": ")
          stop2 = True
          stop3 = False
          while not stop3:
            if user_input.lower() == "weapon stats":
              weapon_stats()
              stop3 = True
            elif user_input.lower() == "continue":
              stop3 = True
              continue
            else:
              print_and_sleep("That's not the correct input!", 2)
              user_input = input("Please try again. : ")
              continue
        else:
          print_and_sleep("That's not the correct input!", 2)
          user_input = input("Please try again. : ")
          continue
    else:
      print_and_sleep("That's not the correct input!", 2)
      user_input = input("Please try again. : ")
      continue

first_time_playing()

