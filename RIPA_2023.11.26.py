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
#11/25/23   Ethan Looper    Made combat function and adjusted move-check function
#                           anc made more comments
#11/26/23   Sean Bolt       Created function which writes player's name, level and whether or not
#                           they won to a file, which can be displayed via another function.
#11/28/23   Sean Bolt       Created healing function and function to get potion

from random import randint

# MAIN FUNCTION TO START AND MANAGE THE GAME
def main():
    # INITIALIZE GAME VARIABLES
    player_entering_discovered = 0 # 1 IF PLAYER ATTEMPTS TO ENTER PREVIOUS ROOM
    room = 0
    game_won = 0

    # PRINT GAME INTRODUCTION AND INSTRUCTIONS
    print("Welcome to the dungeon, adventurer!")
    print("In this game, you will attempt to progress through 10 levels")
    print("On the last level, you must defeat the boss")
    print("User can see player log by entering 0 at combat or movement prompts")
    
    # PLAYER NAME INPUT
    global player_name
    player_name = input("What is your name?:  ")
    print("Good luck, " + player_name + "!")

    # CREATE THE GAME MAP
    create_map()

    # INITIALIZE PLAYER STATS
    global player_stats
    player_stats = [0, 100, 0, 0, 0]  # PLAYER STATS: LEVEL, HEALTH, HEALING POTION AMOUNT, X LOCATION, Y LOCATION
    print("You enter the dungeon")

    # MAIN GAME LOOP
    while game_won == 0:
        if check_move(check_input(5, "m")):
            print("\nYour character moved.")
            print("Location: Room", map.index(2))
        else:
            print("Invalid direction; You weren't able to move. try again")
            print()

#FUNCTION TO PRINT YOURE DEAD
import turtle

def youre_dead(message):
    window = turtle.Screen()
    window.bgcolor("black")

    pen = turtle.Turtle()
    pen.color("red")
    pen.speed(1)

    pen.penup()
    pen.goto(-100,0)
    pen.pendown()

    pen.write(message, font =
              ("Arial", 24, "normal"))

    turtle.done()



#FUNCTION TO PRINT COMBAT SUCCESSFUL
import turtle

def combat_successful(message):
    window = turtle.Screen()
    window.bgcolor("yellow")

    pen = turtle.Turtle()
    pen.color("green")
    pen.speed(1)

    pen.penup()
    pen.goto(-100,0)
    pen.pendown()

    pen.write(message, font =
              ("Arial", 24, "normal"))

    turtle.done()



#FUCNTION THAT PRINTS GAME OVER
import turtle

def game_over(message):
    window = turtle.Screen()
    window.bgcolor("red")

    pen = turtle.Turtle()
    pen.color("black")
    pen.speed(1)

    pen.penup()
    pen.goto(-100,0)
    pen.pendown()

    pen.write(message, font =
              ("Arial", 24, "normal"))

    turtle.done()

game_over("GAME OVER!")

#FUNCTION THAT PRINTS YOU WON
import turtle

def you_won(message):
    window = turtle.Screen()
    window.bgcolor("orange")

    pen = turtle.Turtle()
    pen.color("purple")
    pen.speed(1)

    pen.penup()
    pen.goto(-100,0)
    pen.pendown()

    pen.write(message, font =
              ("Arial", 24, "normal"))

    turtle.done()



# FUNCTION TO VALIDATE PLAYER INPUT
def check_input(option_count, input_type):
    keep_going = True  # SENTINEL FOR INPUT CHECK LOOP
    while keep_going:
        if input_type == "m":  # CHECK IF INPUT TYPE IS FOR MOVEMENT
            user_num = input("Enter a number from 1 to " + str(option_count) + "(1-Left, 2-Down, 3-Right, 5-Up: ")
            if user_num.strip().isdigit():  # CHECK IF INPUT IS A DIGIT
                user_num = int(user_num)  # CONVERT INPUT TO INTEGER
                if user_num == 0:
                    read_data()
                if 1 <= user_num <= option_count:  # VALIDATE INPUT RANGE
                    keep_going = False
                    return user_num
                else:
                    print("Invalid input, please try again")


# FUNCTION TO CHECK PLAYER MOVEMENT
def check_move(direction):
    global player_entering_discovered, map, player_stats  # ACCESS GLOBAL VARIABLES

    player_location = map.index(2)  # FIND PLAYER'S CURRENT LOCATION

    # BOUNDARY CHECKS FOR MOVEMENT
    if direction == 4 or \
       (player_location < 4 and direction == 5) or \
       (player_location % 4 == 0 and direction == 1) or \
       (player_location > 11 and direction == 2) or \
       (player_location % 4 == 3 and direction == 3):
        
        return False

    # CALCULATE NEW LOCATION BASED ON DIRECTION
    new_location = player_location
    if direction == 1:
        new_location -= 1
    elif direction == 2:
        new_location += 4
    elif direction == 3:
        new_location += 1
    elif direction == 5:
        new_location -= 4

    # CHECK FOR UNDISCOVERED ROOMS AND TRIGGER ENEMY ENCOUNTER
    if map[new_location] == 0:
        encounter_result = encounter_enemy()
        if isinstance(encounter_result, tuple):
            room_discovered, updated_health = encounter_result
            player_stats[1] = updated_health  # UPDATE PLAYER HEALTH
        else:
            room_discovered = encounter_result

        if room_discovered:
            map[new_location] = 1  # MARK ROOM AS DISCOVERED
            map[player_location] = 1 if map[player_location] == 2 else map[player_location]
            map[new_location] = 2  # MOVE PLAYER TO NEW LOCATION
            return True
        else:
            # PLAYER RUNS AWAY; NO MOVEMENT
            return False
    else:
        # MOVE PLAYER TO NEW LOCATION IF ALREADY DISCOVERED
        map[player_location] = 1 if map[player_location] == 2 else map[player_location]
        map[new_location] = 2
        return True

import random

# FUNCTION TO HANDLE ENEMY ENCOUNTERS
def encounter_enemy():
    # GENERATE RANDOM NUMBER TO DETERMINE ENEMY TYPE
    enemy_chance = random.randint(1, 100)
    enemy_alive = 1

    # DETERMINE ENEMY TYPE BASED ON RANDOM CHANCE
    if enemy_chance <= 60:  # 60% CHANCE FOR WEAK ENEMY
        enemy_stats = [enemy_alive, 30, 5]  # WEAK ENEMY STATS: [ALIVE, HEALTH, ATTACK]
    elif enemy_chance <= 85:  # 25% CHANCE FOR MEDIUM ENEMY
        enemy_stats = [enemy_alive, 50, 10]  # MEDIUM ENEMY STATS: [ALIVE, HEALTH, ATTACK]
    else:  # 15% CHANCE FOR STRONG ENEMY
        enemy_stats = [enemy_alive, 70, 10]  # STRONG ENEMY STATS: [ALIVE, HEALTH, ATTACK]

    print(f"You encountered an enemy! Health: {enemy_stats[1]}, Attack: {enemy_stats[2]}")

    # INITIALIZE PLAYER HEALTH
    player_health = player_stats[1]

    # COMBAT LOOP
    while enemy_stats[1] > 0:
        player_choice = input("Enter '4' to attack: ")
        if player_choice == '4':
            # PLAYER ATTACKS
            enemy_stats[1] -= 15  # PLAYER ATTACKS ENEMY, REDUCING ENEMY'S HEALTH
            print(f"You attacked the enemy. Enemy health: {enemy_stats[1]}")
            if enemy_stats[1] <= 0:
                print("ENEMY DEFEATED!!")
                return True, player_health  # RETURN TUPLE INDICATING ENEMY DEFEATED AND PLAYER HEALTH

            # ENEMY'S TURN TO ATTACK
            if random.choice([True, False]):  # 50% CHANCE FOR ENEMY TO HIT OR MISS
                player_health -= enemy_stats[2]  # REDUCE PLAYER HEALTH IF ENEMY HITS
                if (player_health <= 0):
                    println("The enemy has defeated you!")
                    write_file(False)
                    youre_dead("YOU'RE DEAD!")
                    break
                print("The enemy attacks you!", "PLAYER HEALTH:", player_health)
            else:
                print("The enemy missed their attack!")

        else:
            print("Invalid input. You missed the opportunity to attack.")
    combat_successful("COMBAT SUCCESSFUL!")
    return True, player_health  # RETURN TUPLE INDICATING ENEMY DEFEATED AND PLAYER HEALTH


# FUNCTION TO CREATE THE GAME MAP
def create_map():
    global map
    map = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # INITIALIZE ALL ROOMS AS UNDISCOVERED (0)

def write_data(win_status):
    player_file = open('player_log.txt', 'a')
    player_file.write(player_name +"\n")
    player_file.write(str(player_stats[0]))
    if (win_status == True):
        player_file.write("Win")
    else:
        player_file.write("Loss")
    player_file.close()
    
def read_data():
    player_file = open('player_log.txt', 'r')
    text_line = player_file.readline()
    while (text_line != ''):
        print(text_line)
        text_line = player_file.readline()
    player_file.close()
    
def heal():
    if player_stats[1]<100:#is player missing health
        if player_stats[2]>0:#do they have potions?
            player_stats[1]+=15#heal player
            player_stats[2]-=1#take potion
            print("You healed 15 HP")

def get_potions():
    potion_roll = random.randint(0, 100)
    if potion_roll < 50:
        print("0 potions obtained")
    elif potion_roll < 80:
        player_stats[2]+=1
        print("1 potions obtained")
    elif potion_roll < 95:
        player_stats[2]+=2
        print("2 potions obtained")
    else:
        player_stats[2]+=3
        print("2 potions obtained")

# START THE GAME
main()

