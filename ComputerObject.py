import random
from ShipsObject import *
from StringConversions import *

class Computer(object):
    
    def __init__(self):
        self.mode = "Seek"
        self.hits = []
        self.letters = ["A","B","C","D","E","F","G","H","I","J"]
        self.numbers = ["1","2","3","4","5","6","7","8","9","10"]
        self.sunkships = 0
        self.indicator = 0
        
    def choose_square(self):
        self.row = random.choice(["A","B","C","D","E","F","G","H","I","J"])
        self.col = random.choice(["1","2","3","4","5","6","7","8","9","10"])
        return self.row, self.col
    
    def change_mode(self):
        if self.mode == "Seek":
            self.mode = "Destroy"
        else:
            self.mode = "Seek"
    
    def choose_square_AI(self):
        if self.mode == "Seek":
           #self.row = random.choice(["A","B","C","D","E","F","G","H","I","J"])
           #self.col = random.choice(["1","2","3","4","5","6","7","8","9","10"]) 
           blah = random.randint(0,4)
           if blah == 1 or blah == 3:
               self.row = random.choice(["A","C","E","G","I"])
               self.col = random.choice(["1","3","5","7","9"])
           elif blah == 0 or blah == 2:
               self.row = random.choice(["B","D","F","H","J"])
               self.col = random.choice(["2","4","6","8","10"])
           else:
               self.row = random.choice(["A","B","C","D","E","F","G","H","I","J"])
               self.col = random.choice(["1","2","3","4","5","6","7","8","9","10"])
        else:
            (arg1, arg2) = random.choice(self.hits)
            # ensure that it doesn't check the other side of the board whilst seeking to destroy
            if arg1 == 9:
                vh = random.randint(0,1)
                if vh == 1:
                    matrix1 = [self.letters[arg1]]
                    matrix2 = [self.numbers[arg2 + 1], self.numbers[arg2 - 1]]
                else:
                    matrix1 = [self.letters[arg1 - 1]]
                    matrix2 = [self.numbers[arg2]]
            elif arg1 == 0:
                vh = random.randint(0,1)
                if vh == 1:
                    matrix1 = [self.letters[arg1]]
                    matrix2 = [self.numbers[arg2 + 1], self.numbers[arg2 - 1]]
                else:
                    matrix1 = [self.letters[arg1 + 1]]
                    matrix2 = [self.numbers[arg2]]
            elif arg2 == 0:
                vh = random.randint(0,1)
                if vh == 1:
                    matrix1 = [self.letters[arg1]]
                    matrix2 = [self.numbers[arg2 + 1]]
                else:
                    matrix1 = [self.letters[arg1 + 1], self.letters[arg1 - 1]]
                    matrix2 = [self.numbers[arg2]]
            elif arg2 == 9:
                vh = random.randint(0,1)
                if vh == 1:
                    matrix1 = [self.letters[arg1]]
                    matrix2 = [self.numbers[arg2 + 1]]
                else:
                    matrix1 = [self.letters[arg1 + 1], self.letters[arg1 - 1]]
                    matrix2 = [self.numbers[arg2]]
            else:
                vh = random.randint(0,1)
                if vh == 1:
                    matrix1 = [self.letters[arg1]]
                    matrix2 = [self.numbers[arg2 + 1], self.numbers[arg2 - 1]]
                else:
                    matrix1 = [self.letters[arg1 + 1], self.letters[arg1 - 1]]
                    matrix2 = [self.numbers[arg2]]
            self.row = random.choice(matrix1)
            self.col = random.choice(matrix2)
        return self.row, self.col
    
    def choose_orientation(self):
        rand = random.randint(0,1)
        if rand == 0:
            self.orientation = "v"
        else:
            self.orientation = "h"
        return self.orientation
        
    def enter_ship_user(self, ship):
        self.ship = ship
        [self.row, self.col] = self.choose_square()
        self.orientation = self.choose_orientation()
        return self.row, self.col, self.orientation, self.ship
    
    def count_sunk(self):
        self.count = 0
        self.indicator = 0
        for ship in all_ships:
            if ship.sunk == True:
                self.count += 1
        if self.sunkships < self.count:
            self.indicator = 1
            self.sunkships = self.count
        

my_computer = Computer()