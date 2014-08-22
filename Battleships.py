"""
So at the moment I'm not entirely sure what format I want this to take but I was thinking about making the following classes:

Board
- Checks move validity
- Adds move onto the board
- Provides a winner query
- Represents hit and miss with different items
- 10 x 10 (or n x n)

Ships
- Construct the different ships (size 5,4,3,3,2?)
- Define orientation to be horizontal or vertical
- Define placement of ships
- Check if ship has been hit

Player
- Allows player to guess positions

"""

import random
from ShipsObject import *
from PlayerObjecty import *
from ComputerObject import *
from BoardObject import *
from StringConversions import *

def hit_or_miss(user):
    if user == my_player:
        player_guess.guess_coord(user)
        player_guess.store_coords(player_guess.coordmatrix)
        if (player_guess.row, player_guess.col) in comp_ships.coordmatrix:
           player_guess.board[player_guess.row][player_guess.col] = "X"
           comp_ships.board[player_guess.row][player_guess.col] = "X"
           for ship in all_shipsC:
               check_ship(ship, user)
           player_guess.boardhits += 1
        else:
           player_guess.board[player_guess.row][player_guess.col] = "O"
           comp_ships.board[player_guess.row][player_guess.col] = "O"  
    else:
        comp_guess.guess_coord(user)
        comp_guess.store_coords(comp_guess.coordmatrix)
        if (comp_guess.row, comp_guess.col) in player_ships.coordmatrix:
           comp_guess.board[comp_guess.row][comp_guess.col] = "X"
           player_ships.board[comp_guess.row][comp_guess.col] = "X"
           my_computer.hits.append((comp_guess.row, comp_guess.col))
           for ship in all_ships:
               check_ship(ship, user)
           comp_mode()
           comp_guess.boardhits += 1
        else:
           comp_guess.board[comp_guess.row][comp_guess.col] = "O"
           player_ships.board[comp_guess.row][comp_guess.col] = "O"

def comp_mode():
    if my_computer.mode == "Seek":
        my_computer.change_mode()
    else:
       my_computer.count_sunk()
       if my_computer.indicator == 1:
           my_computer.change_mode()

def check_ship(ship, user):
    if user == my_player:
        if (player_guess.row, player_guess.col) in ship.coordmatrix:
            ship.hitcount += 1
    if user == my_computer:
        if (comp_guess.row, comp_guess.col) in ship.coordmatrix:
            ship.hitcount += 1
    if ship.hitcount == ship.size:
        ship.sunk = True

def ships_sunk():
    print
    count = 0
    for ship in all_shipsC:
        if ship.sunk == True:
            print "The " + ship.name + " ship has been sunk by you"
    for ship in all_ships:
        if ship.sunk == True:
            count += 1
            print "The " + ship.name + " ship has been sunk by the computer"
    return count

def winner_query():
    if comp_guess.boardhits < 17 and player_guess.boardhits < 17:
        winner = False
    else:
        if comp_guess.boardhits < 17:
            print "Congrats dude. You win"
        else:
            print "You loser. Suckerrrrrrrr!"
        winner = True
    return winner

def ship_placement():
    comp_ships.add_all_ships_stage_2(my_computer)
    comp_ships.print_board()
    #player_ships.add_all_ships_stage_2(my_computer) # hard coded to randomise
    player_ships.add_all_ships_stage_2(my_player)

def play_game():
    winner = False
    whos_turn = 0
    ship_placement()
    for ship in all_ships:
        print ship.coordmatrix
    for ship in all_shipsC:
        print ship.coordmatrix
    while winner == False:
        while whos_turn == 0: # player's turn
            print "You can see which guesses are hits and which are misses"
            print " Please take your guess" + "\n"
            ships_sunk()
            player_guess.print_board()
            hit_or_miss(my_player)
            if winner_query() == True:
                player_guess.print_board()
                winner = True
                break
            whos_turn = 1
        while whos_turn == 1:
            hit_or_miss(my_computer)
            print my_computer.mode
            print " The computer has taken its turn"
            print " This is the board your ships are placed in. You can see the hits and misses." + "\n"
            player_ships.print_board()
            if winner_query() == True:
                player_ships.print_board()
                winner = True
                break
            whos_turn = 0

play_game()
    