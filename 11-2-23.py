import random

# You have entered room AAA111 , there is ___
    # no enemy
    # an

# Room ID LIST
    # XXX ARRAY WITH [X value, Y value, Was this room discovered(True / False]
        # If room not discovered:
            # Randomize Room Traits (Enemy chance 1-100 / Loot chance 1-500 / etc)
                #For Enemies (If random value is in range)(If range >= 40, enter ENCOUNTER FUNCTION)
                    #1-40   No Enemy Spawn
                    #41-60  Weak Enemy Spawn
                    #61-95  Medium Enemy Spawn
                    #96-100 Strong Enemy Spawn
                        #If value >= 40 : ENCOUTER Function
                            #Prompt for inputs "4" for Attack, "6" for Heal
                            #After each input get random value (1-3) for what enemy will do
                                #If 1, Attack   (-20 Player health)
                                #If 2, Nothing
                                #If 3, Heal     (+10 Enemy Health)
                            #If enemy health <1 then Resume input function
                            #If player health <1 then close out of program, Populate (You Die)
                #For Loot (Random value)
                    #1-100      No Loot
                    #101-350    Small Loot  (+5 Gold)
                    #351-450    Medium Loot (+20 Gold)
                    #451-500    Large Loot  (+50 Gold)
                        #If loot is >100, add GOLD to Stats List
        #If Room discovered (True) resume function to prompt for input
# Stats

# make another function where if the list value / variable "discovered == 0, then a function that randomizes a chance of an "encounter" which will be printed. There is a 50 percent chance of an encounter, which will be determined by using a range function with a randomint that makes anumber between 1-100. if the range is within 1-50, no encounter happens. if the range is from 51-100 than it happens. each encounter will have an enemy will a list 

# Prompt (What are you going to do)

from random import randint  # Make sure to import randint

x_value = 0
y_value = 0
discovered = 0
game_win = 0

def movement(x_value, y_value, discovered, game_win):
    room_id = [x_value, y_value, discovered]
    enemy_alive = 0
    enemy_health = 0
    enemy_attack = 0
    enemy_stats = [enemy_alive, enemy_health, enemy_attack]
    
    while game_win == 0:
        player_input = int(input(" [1] Left [5] Forward [2] Backward [3] Right "))
        if player_input == 1:
            x_value -= 1
        elif player_input == 2:
            y_value -= 1
        elif player_input == 3:
            x_value += 1
        elif player_input == 5:
            y_value += 1
        room_id[0] = x_value
        room_id[1] = y_value
        print(f"Current location: {room_id}")
        
        # Chance encounter logic after each movement
        chance_encounter = randint(1, 100)
        if chance_encounter < 50:
            enemy_alive = 1
            enemy_health += 100
            print("An enemy spawned!")
            enemy_stats = [enemy_alive, enemy_health, enemy_attack]
            print(f"Enemy stats: {enemy_stats}")
        else:
            print("No enemies encountered.")

# Call the movement function with initial values
movement(x_value, y_value, discovered, game_win)

# LIST FOR 
