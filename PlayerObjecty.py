from ShipsObject import *
from StringConversions import *

class Player(object):
    
    def __init__(self):
         pass
         
    def choose_square(self):
        check1 = False
        check2 = False
        while check1 == False:
            self.row = raw_input("Please enter a row (A-J): ")
            self.row = self.row.upper()
            if len(self.row) > 1 or len(self.row) == 0:
                print "This is invalid input."
            else:
                check1 = True
        while check2 == False:
            self.col = raw_input("Please enter a column (1-10): ")
            catch = " "
            try:
                catch = int(self.col)
            except:
                print "This needs to be an integer you fool!"
            if catch in range(1,11):
                check2 = True
            else:
                print "This number is out of range you cretin!"
        return self.row, self.col
    
    def choose_square_AI(self):
        # copied so that I can write the AI for the computer and maintain function names
        self.choose_square()
    
    def choose_orientation(self):
        self.orientation = " "
        while self.orientation != "v" and self.orientation != "h":
            blah = raw_input("Please choose orientation for ship. V(ertical) / H(orizontal): ")
            blah = blah[0]
            self.orientation = blah.lower()
        return self.orientation
    
    def enter_ship_user(self, ship):
        print "Please select coordinates for " + ship.name + " ship"
        self.ship = ship
        [self.row, self.col] = self.choose_square()
        self.orientation = self.choose_orientation()
        return self.row, self.col, self.orientation, self.ship

        
my_player = Player()

