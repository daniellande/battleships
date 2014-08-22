import random
from ShipsObject import *
from PlayerObjecty import *
from StringConversions import *
from ComputerObject import *


class Board(object):
    
    def __init__(self):
        self.A = [' '] * 10
        self.B = [' '] * 10
        self.C = [' '] * 10
        self.D = [' '] * 10
        self.E = [' '] * 10
        self.F = [' '] * 10
        self.G = [' '] * 10
        self.H = [' '] * 10
        self.I = [' '] * 10
        self.J = [' '] * 10
    
        self.board = [self.A,self.B,self.C,self.D,self.E,self.F,self.G,self.H,self.I,self.J]
        self.coordmatrix = []
        self.boardhits = 0
        
    def store_coords(self, coordmatrix):
        self.coordmatrix.append((self.row,self.col))
        return self.coordmatrix
    
    def will_ship_fit(self, user):
        self.indicator1 = False
        self.row = char_conversion(user.row)
        self.col = num_conversion(user.col)
        if user.orientation == "h":
            if self.col + user.ship.size > 10:
                return self.indicator1
            else:
                self.indicator1 = True
                return self.indicator1, self.row, self.col
        else:
            if self.row + user.ship.size > 10:
                return self.indicator1
            else:
                self.indicator1 = True
                return self.indicator1, self.row, self.col
    
    def is_space_free(self,user):
        self.indicator2 = False
        if self.indicator1 == True:
            count = 0
            for i in range(user.ship.size):
                if user.orientation == "h":
                    if self.board[self.row][self.col + i] == " ":
                        count += 1
                else:
                    if self.board[self.row + i][self.col] == " ":
                        count += 1
            if count == user.ship.size:
                self.indicator2 = True
        return self.indicator2
        
    def add_to_board(self, user):
        self.addbinary = False
        self.will_ship_fit(user)
        self.is_space_free(user)
        if self.indicator1 == True and self.indicator2 == True and user.orientation == "h":
            for i in range(user.ship.size):
                self.board[self.row][self.col + i] = user.ship.marker
                self.coordmatrix.append((self.row, self.col + i))
                user.ship.coordmatrix.append((self.row, self.col + i))
            self.addbinary = True
            return self.addbinary
        elif self.indicator1 == True and self.indicator2 == True and user.orientation == "v":
            for i in range(user.ship.size):
                self.board[self.row + i][self.col] = user.ship.marker
                self.coordmatrix.append((self.row + i, self.col))
                user.ship.coordmatrix.append((self.row + i, self.col))
            self.addbinary = True
            return self.addbinary
        else:
            if user == my_player:
                print "Ship can not be placed here motherfuckers"
            self.addbinary = False
            return self.addbinary
    
    def guess_coord(self, user):
        indicator = False
        while indicator == False:
            user.choose_square_AI()
            self.row = char_conversion(user.row)
            self.col = num_conversion(user.col)
            if self.row in range(0,9) and self.col in range(0,9):
                pass
            else:
                print "This input is not inside the board"
            if (self.row, self.col) in self.coordmatrix:
                print "This value has already been guessed"
            else:
                indicator = True
        return self.row, self.col
        
    def add_all_ships(self, user, ship):
        self.indicator3 = False
        while self.indicator3 == False:
            user.enter_ship_user(ship)
            self.add_to_board(user)
            if user == my_player:
                self.print_board()
            if self.addbinary == True:
                self.indicator3 = True
        return self.indicator3
        
    def add_all_ships_stage_2(self, user):
        if user == my_computer:
            for ship in all_shipsC:
                self.add_all_ships(user, ship)
        else:
            for ship in all_ships:
                self.add_all_ships(user, ship)
        
    
    def print_board(self):
        print
        print  "       1     2     3     4     5     6     7     8     9     10  "
        print ("     ------------------------------------------------------------")
        print  " A  |  "+ self.board[0][0]  + "  |  " +  self.board[0][1]  + "  |  " +  self.board[0][2]  + "  |  " +  self.board[0][3]  + "  |  " +  self.board[0][4]  + "  |  " +  self.board[0][5]  + "  |  " +  self.board[0][6]  + "  |  " +  self.board[0][7]  + "  |  " +  self.board[0][8]  + "  |  " +  self.board[0][9]  + "  |  "
        print ("     ------------------------------------------------------------")
        print  " B  |  "+ self.board[1][0]  + "  |  " +  self.board[1][1]  + "  |  " +  self.board[1][2]  + "  |  " +  self.board[1][3]  + "  |  " +  self.board[1][4]  + "  |  " +  self.board[1][5]  + "  |  " +  self.board[1][6]  + "  |  " +  self.board[1][7]  + "  |  " +  self.board[1][8]  + "  |  " +  self.board[1][9]  + "  |  "
        print ("     ------------------------------------------------------------")
        print  " C  |  "+ self.board[2][0]  + "  |  " +  self.board[2][1]  + "  |  " +  self.board[2][2]  + "  |  " +  self.board[2][3]  + "  |  " +  self.board[2][4]  + "  |  " +  self.board[2][5]  + "  |  " +  self.board[2][6]  + "  |  " +  self.board[2][7]  + "  |  " +  self.board[2][8]  + "  |  " +  self.board[2][9]  + "  |  "
        print ("     ------------------------------------------------------------")
        print  " D  |  "+ self.board[3][0]  + "  |  " +  self.board[3][1]  + "  |  " +  self.board[3][2]  + "  |  " +  self.board[3][3]  + "  |  " +  self.board[3][4]  + "  |  " +  self.board[3][5]  + "  |  " +  self.board[3][6]  + "  |  " +  self.board[3][7]  + "  |  " +  self.board[3][8]  + "  |  " +  self.board[3][9]  + "  |  "
        print ("     ------------------------------------------------------------")
        print  " E  |  "+ self.board[4][0]  + "  |  " +  self.board[4][1]  + "  |  " +  self.board[4][2]  + "  |  " +  self.board[4][3]  + "  |  " +  self.board[4][4]  + "  |  " +  self.board[4][5]  + "  |  " +  self.board[4][6]  + "  |  " +  self.board[4][7]  + "  |  " +  self.board[4][8]  + "  |  " +  self.board[4][9]  + "  |  "
        print ("     ------------------------------------------------------------")
        print  " F  |  "+ self.board[5][0]  + "  |  " +  self.board[5][1]  + "  |  " +  self.board[5][2]  + "  |  " +  self.board[5][3]  + "  |  " +  self.board[5][4]  + "  |  " +  self.board[5][5]  + "  |  " +  self.board[5][6]  + "  |  " +  self.board[5][7]  + "  |  " +  self.board[5][8]  + "  |  " +  self.board[5][9]  + "  |  "
        print ("     ------------------------------------------------------------")
        print  " G  |  "+ self.board[6][0]  + "  |  " +  self.board[6][1]  + "  |  " +  self.board[6][2]  + "  |  " +  self.board[6][3]  + "  |  " +  self.board[6][4]  + "  |  " +  self.board[6][5]  + "  |  " +  self.board[6][6]  + "  |  " +  self.board[6][7]  + "  |  " +  self.board[6][8]  + "  |  " +  self.board[6][9]  + "  |  "
        print ("     ------------------------------------------------------------")
        print  " H  |  "+ self.board[7][0]  + "  |  " +  self.board[7][1]  + "  |  " +  self.board[7][2]  + "  |  " +  self.board[7][3]  + "  |  " +  self.board[7][4]  + "  |  " +  self.board[7][5]  + "  |  " +  self.board[7][6]  + "  |  " +  self.board[7][7]  + "  |  " +  self.board[7][8]  + "  |  " +  self.board[7][9]  + "  |  "
        print ("     ------------------------------------------------------------")
        print  " I  |  "+ self.board[8][0]  + "  |  " +  self.board[8][1]  + "  |  " +  self.board[8][2]  + "  |  " +  self.board[8][3]  + "  |  " +  self.board[8][4]  + "  |  " +  self.board[8][5]  + "  |  " +  self.board[8][6]  + "  |  " +  self.board[8][7]  + "  |  " +  self.board[8][8]  + "  |  " +  self.board[8][9]  + "  |  "
        print ("     ------------------------------------------------------------")
        print  " J  |  "+ self.board[9][0]  + "  |  " +  self.board[9][1]  + "  |  " +  self.board[9][2]  + "  |  " +  self.board[9][3]  + "  |  " +  self.board[9][4]  + "  |  " +  self.board[9][5]  + "  |  " +  self.board[9][6]  + "  |  " +  self.board[9][7]  + "  |  " +  self.board[9][8]  + "  |  " +  self.board[9][9]  + "  |  "
        print ("     ------------------------------------------------------------")

player_ships = Board()
player_guess = Board()
comp_guess = Board()
comp_ships = Board()