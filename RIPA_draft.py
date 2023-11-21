#The Silver Bullets
#Ethan Looper, Chatham Stokes, Sean Bolt
#Unnamed Choose your own adventure dungeon crawler RPG
#Inputs: User inputs Player Name, inputs player choices based of prompts
#Outputs: 
#Change Log
#Date       Programmer      Description
#--------------------------------------
#10/12/23   Sean Bolt       Created file, collaboated to make single-input
#                           program where user is able to enter name, also
#                           prints starting contextual information
#10/24/23   Sean Bolt       Created an input validation function to be called in 
#                           other functions and main
#10/24/23   Sean Bolt       Created array variable which holds various player
#                           attributes, such as their level and health, also
#                           starting player room info and map array 
#10/29/23   All             Created definitions for a few functions as well as 
#                           repitition and decision stuctures in user input validation loop
#11/2/23    Ethan Looper    Created navigation functions and beginning combat functions
#11/9/23    Sean Bolt       Made player not able to exit map via check_move function


from random import randint
def main():
  player_entering_discovered = 0 #1 if player attempts to enter previous room
  room = 0
  game_won = 0
  print("Welcome to the dungeon, adventurer!")
  print("In this game, you will attempt to progress through 10 levels")
  print("On the last level, you must defeat the boss")
  print("Player level determines combat success chance")
  print("The player can choose to fight or flee from all combats except boss")
  player_name = input("What is your name?")
  print("Good luck, " +player_name+"!")
  create_map()
  global player_stats
  player_stats= [0, 100, 0, 0, 0]#level, health, healing potion amount 
  #healing potion amount, X location, Y location
  print("You enter the dungeon")
  while game_won == 0:
    if check_move(check_input(5, "m")):
      print("Your character moved.")
      print(map.index(2))
    else:
      print("Invalid direction, try again")


def check_input(option_count, input_type):#function definition for input validation
  keep_going = True#sentinel for input check loop
  #Input type is "m" or "c" for movement or combat
  while keep_going == True:
    if (input_type == "m"):#not necessary if only needing ints, but might need other type inputs later
      user_num = input("Enter a number from 1 to "+str(option_count)+"(1-Left, 2-Down, 3-Right, 5-Up")#user input 
      if user_num.strip().isdigit():#checks if input is string
        user_num = int(user_num)#makes input into int
        if user_num <=option_count and user_num >=1:#check for correct input
          keep_going = False
          return user_num
        else:
          print("Invalid input, please try again")
          
def check_move(direction):#1 left, 2 down, 3 right, 5 up
    player_location = map.index(2)
    print(player_location)
    if direction == 4:
        return False
    if player_location < 4 and direction == 5:
        return False
    elif player_location % 4 == 0 and direction == 1:
        return False
    elif player_location > 11 and direction == 2:
        return False
    elif player_location %4 == 3 and direction == 3:
        return False
    else:
        try:
          if direction == 1:
              if map[player_location - 1] == 1:
                player_entering_discovered = 1
                map[player_location - 1] = 2
                map[player_location] = 1
              else:
                player_entering_discovered = 0
                map[player_location - 1] = 2
                map[player_location] = 1
          if direction == 2:
              if map[player_location + 4] == 1:
                player_entering_discovered = 1
                map[player_location + 4] = 2
                map[player_location] = 1
              else:
                player_entering_discovered = 0
                map[player_location + 4] = 2
                map[player_location] = 1
          if direction == 3:
              if map[player_location + 1] == 1:
                player_entering_discovered = 1
                map[player_location + 1] = 2
                map[player_location] = 1
              else:
                player_entering_discovered = 0
                map[player_location + 1] = 2
                map[player_location] = 1
          if direction == 5:
              if map[player_location -4] == 1:
                player_entering_discovered = 1
                map[player_location - 4] = 2
                map[player_location] = 1
              else:
                player_entering_discovered = 0
                map[player_location - 4] = 2
                map[player_location] = 1
        except IndexError:
          print("Invalid direction, try again")
          return False
        return True
    print(player_entering_discovered)
    print(player_location)

def create_map():
    #fills list with 0 to represent unexplored rooms. When explored, will change to 1
    global map
    map = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]














main()
