import time
from classes import *
import string 

def print_and_sleep(text, seconds):
  print(text)
  time.sleep(seconds)

def first_time_playing():
  print_and_sleep("Welcome to Console Slayer!", 2)
  print_and_sleep("Before we can start, we are going to need a name.", 2)
  player.name = input("Slayer, what is your name? : ")
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

first_time_playing()