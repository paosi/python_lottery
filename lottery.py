#!/usr/bin/env python3

import random

# Lottery Game and Winning Number Generator

# Pick 3 generates three numbers from 0-9. Winning numbers can be duplicated, eg. 2, 2, 2
def pick3():
    picks = []
    num_range = range(0, 10)
    all_balls = list(num_range)
    i = 0
    while i < 3:
        draw = random.choice(all_balls)
        picks.append(draw)
        i += 1
    return picks

# The player chooses their numbers and it is compared with the winning numbers
def play_pick3():
    picks = pick3()
    player_picks = []
    i = 0
    while i < 3:
        try:
            guess = int(input("Pick a number from 0-9: "))
        except ValueError:
            # Eliminates errors if the user inputs a non-integer
            print("INPUT MUST BE A NUMBER")
        else:
            if guess in range(0, 10):
                player_picks.append(guess)
                i += 1
            else:
                # User picked a number outside the range
                print("INVALID NUMBER")
    print("Your numbers are:",(', '.join(map(str, player_picks))))
    print("Tonight's winning numbers are:",(', '.join(map(str, picks))))

    # Check to see how many matches there are and return that number
    match = 0
    for num in picks:
        if num in player_picks:
            match += 1 
            picks.remove(num)
            player_picks.remove(num)
    if match == 1:
        print("You have {x} match".format(x = match))
    else:
        print("You have {x} matches".format(x = match))

    # Check to see if all the numbers match
    if sorted(picks) == sorted(player_picks):
        print("JACKPOT!!!")
    else:
        print("Try again")


# Pick 6 generates six numbers from 1-49. Winning numbers can only be chosen once, eg. 1, 2, 3, 4, 5, 6
def pick6():
    picks = []
    num_range = range(1, 50)
    all_balls = list(num_range)
    i = 0
    while i < 6:
        draw = random.choice(all_balls)
        picks.append(draw)
        all_balls.remove(draw)
        i += 1
    return picks    

# The player chooses their numbers and it is compared with the winning numbers
def play_pick6():
    picks = pick6()
    player_picks = []
    num_range = range(1, 50)
    all_balls = list(num_range) 
    i = 0
    while i < 6:
        try:
            guess = int(input("Pick a number from 1-49: "))
        except ValueError:
            # Eliminates errors if the user inputs a non-integer
            print("INPUT MUST BE A NUMBER")
        else:
            if guess in range(1, 50):
                if guess in all_balls:
                    player_picks.append(guess)
                    all_balls.remove(guess)
                    i += 1
                else:
                    print("Number Already Chosen")
            else:
                # User picked a number outside the range
                print("INVALID NUMBER")
    
    print("Your numbers are:",(', '.join(map(str, player_picks))))
    print("Tonight's winning numbers are:",(', '.join(map(str, picks))))

    # Check to see how many matches there are and return that number
    match = 0
    for num in picks:
        if num in player_picks:
            match += 1 
    if match == 1:
        print("You have {x} match".format(x = match))
    else:
        print("You have {x} matches".format(x = match))

    # Check to see if all the numbers match
    if sorted(picks) == sorted(player_picks):
        print("JACKPOT!!!")
    else:
        print("Try again")


# Mega Millions generates five numbers from 1-70 and one "Moneyball" from 1-25
# The moneyball can be a duplicate of one of the previous five numbers
def mega_millions():
    num_balls = 5
    picks = []
    num_range = range(1, 71)
    all_balls = list(num_range)
    i = 0
    while i < num_balls:
        draw = random.choice(all_balls)
        picks.append(draw)
        all_balls.remove(draw)
        i += 1
    moneyball = random.randint(1, 25)
    picks.append(moneyball)
    return picks

# The player chooses their numbers and it is compared with the winning numbers
def play_mega():
    picks = mega_millions()
    player_picks = []
    num_range = range(1, 71)
    all_balls = list(num_range) 
    i = 0
    j = 0
    while i < 5:
        try:
            guess = int(input("Pick a number from 1-70: "))      
        except ValueError:
            # Eliminates errors if the user inputs a non-integer
            print("INPUT MUST BE A NUMBER")
        else:
            if guess in range(1, 71):
                if guess in all_balls:
                    player_picks.append(guess)
                    all_balls.remove(guess)
                    i += 1
                else:
                    print("Number Already Chosen")
            else:
                # User picked a number outside the range
                print("INVALID NUMBER")
    while j < 1:
        try:
            guess_moneyball = int(input("-MONEYBALL- Pick a number from 1-25: "))
        except ValueError:
            print("INPUT MUST BE A NUMBER")
        else:
            if guess_moneyball in range(1, 26):
                player_picks.append(guess_moneyball)
                j += 1
            else:
                print("INVALID NUMBER")

    print("Your numbers are: {x}, Moneyball: {y}".format(x = (', '.join(map(str, player_picks[0:5]))), y = player_picks[5]))
    print("Tonight's winning numbers are: {x}, Moneyball: {y}".format(x = (', '.join(map(str, picks[0:5]))), y = picks[5]))

    # Check to see how many matches there are and return that number
    match = 0
    for num in picks[0:4]:
        if num in player_picks[0:4]:
            match += 1 
    if match == 1:
        if picks[5] == guess_moneyball:
            print("You have {x} match and you matched the Moneyball")
        else:
            print("You have {x} match".format(x = match))
        print("Try again")
    elif match == range(2, 5) and picks[5] == guess_moneyball:
        print("You have {x} matches and you matched the Moneyball".format(x = match))  
        print("Try again")
    elif match == 5 and picks[5] == guess_moneyball:
        print("JACKPOT!!!")
    elif picks[5] == guess_moneyball:
        print("You matched the Moneyball")
    else:
        print("You have {x} matches".format(x = match))
        print("Try again")


# Powerball generates five numbers from 1-69 and one "Moneyball" from 1-26
# The moneyball can be a duplicate of one of the previous five numbers
def powerball():
    num_balls = 5
    picks = []
    num_range = range(1, 70)
    all_balls = list(num_range)
    i = 0
    while i < num_balls:
        draw = random.choice(all_balls)
        picks.append(draw)
        all_balls.remove(draw)
        i += 1
    moneyball = random.randint(1, 26)
    picks.append(moneyball)

    return picks

def play_power():
    picks = powerball()
    player_picks = []
    num_range = range(1, 70)
    all_balls = list(num_range) 
    i = 0
    j = 0

    while i < 5:
        try:
            guess = int(input("Pick a number from 1-69: "))
        except ValueError:
            # Eliminates errors if the user inputs a non-integer
            print("INPUT MUST BE A NUMBER")
        else:
            if guess in range(1, 70):
                if guess in all_balls:
                    player_picks.append(guess)
                    all_balls.remove(guess)
                    i += 1
                else:
                    print("Number Already Chosen")
            else:
                # User picked a number outside the range
                print("INVALID NUMBER")
    while j < 1:
        try:
            guess_moneyball = int(input("-MONEYBALL- Pick a number from 1-26: "))
        except ValueError:
            print("INPUT MUST BE A NUMBER")
        else:
            if guess_moneyball in range(1, 27):
                player_picks.append(guess_moneyball)
                j += 1
            else:
                print("INVALID NUMBER")

    print("Your numbers are: {x}, Moneyball: {y}".format(x = (', '.join(map(str, player_picks[0:5]))), y = player_picks[5]))
    print("Tonight's winning numbers are: {x}, Moneyball: {y}".format(x = (', '.join(map(str, picks[0:5]))), y = picks[5]))

    # Check to see how many matches there are and return that number
    match = 0
    for num in picks[0:4]:
        if num in player_picks[0:4]:
            match += 1 
    if match == 1:
        if picks[5] == guess_moneyball:
            print("You have {x} match and you matched the Moneyball")
        else:
            print("You have {x} match".format(x = match))
        print("Try again")
    elif match == range(2, 5) and picks[5] == guess_moneyball:
        print("You have {x} matches and you matched the Moneyball".format(x = match))  
        print("Try again")
    elif match == 5 and picks[5] == guess_moneyball:
        print("JACKPOT!!!")
    elif picks[5] == guess_moneyball:
        print("You matched the Moneyball")
    else:
        print("You have {x} matches".format(x = match))
        print("Try again")


def main():
    # The user chooses which game to play
    game = input("Which game do you want to play: Pick 3, Pick 6, Mega Millions, or Powerball? --> ")
    # Re-format the variable for consistency
    game = game.lower()
    game = game.replace(" ","")

    # The correct funcion is chosen according to user input
    if game == "pick3":
        play_pick3()   
    elif game == "pick6":
        play_pick6()
    elif game == "megamillions":
        play_mega()
    elif game == "powerball":
        play_power()
    else:
        print("GAME NOT FOUND")

main()
