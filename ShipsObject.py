class Ships(object):
        
    def __init__(self, size, marker, name, coordmatrix, hitcount, sunk):
        self.size = size
        self.marker = marker
        self.name = name
        self.coordmatrix = coordmatrix
        self.hitcount = 0
        self.sunk = False

AircraftCarrier = Ships(5,"A", "Aircraft Carrier", [], 0, False)
Battleship = Ships(4,"B", "Battleship", [], 0, False)
Submarine = Ships(3,"S", "Submarine", [], 0, False)
Cruiser = Ships(3,"C", "Cruiser", [], 0, False)
Destroyer = Ships(2,"D", "Destroyer", [], 0, False)

all_ships = [AircraftCarrier, Battleship, Submarine, Cruiser, Destroyer]

AircraftCarrierC = Ships(5,"A", "Aircraft Carrier", [], 0, False)
BattleshipC = Ships(4,"B", "Battleship", [], 0, False)
SubmarineC = Ships(3,"S", "Submarine", [], 0, False)
CruiserC = Ships(3,"C", "Cruiser", [], 0, False)
DestroyerC = Ships(2,"D", "Destroyer", [], 0, False)

all_shipsC = [AircraftCarrierC, BattleshipC, SubmarineC, CruiserC, DestroyerC]