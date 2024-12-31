from items import SparePart, ShipPiece, Portal
from random import randint
from random import choice

class Planet:
    BROKEN_PIECE_IMAGES = ["./Img/cabin_broken.ppm", "./Img/exhaust_broken.ppm", "./Img/engine_broken.ppm"]
    WORKING_PIECE_IMAGES = ["./Img/cabin.ppm", "./Img/exhaust.ppm", "./Img/engine.ppm"]
    PIECES_IMAGES = ["./Img/screw.ppm", "./Img/gear.ppm", "./Img/lettuce.ppm", "./Img/bagel.ppm", "./Img/cake.ppm"]
    PORTAL_IMAGES = ["./Img/portal.ppm", "./Img/portal_flashing.ppm"]
    def __init__(self, size=15, starting=False):
        """Initializes a new planet object from a size and boolean indicating if its a starting map

        Args:
            size (int, optional): Represents the side length of the map. Defaults to 15.
            starting (bool, optional): Represents whether or not the map is the starting one. Defaults to False.
        """
        # TODO Part 1
        # Make the following instance fields
        # 1) The map is a size x size 2D Python list
        self.map = [[None for j in range(size)] for i in range(size)]
        
        
        # If its the starting planet
        # Setup the starting map (when starting is True)
        # It has spaceship components, spare parts, and wormholes
        self.starting = starting
        if starting:
            self.map[int(size/2)][int(size/2)] = ShipPiece(Planet.BROKEN_PIECE_IMAGES[1], "broken")
            self.map[int(size/2)][int(size/2)+1] = ShipPiece(Planet.BROKEN_PIECE_IMAGES[1], "broken")
            self.map[int(size/2)-1][int(size/2)] = ShipPiece(Planet.BROKEN_PIECE_IMAGES[2], "broken")
            self.map[int(size/2)+1][int(size/2)] = ShipPiece(Planet.BROKEN_PIECE_IMAGES[2], "broken")
            self.map[int(size/2)][int(size/2)-1] = ShipPiece(Planet.BROKEN_PIECE_IMAGES[0], "broken")
        
        for i in Planet.PIECES_IMAGES:
            p = self.getEmptyLocation()
            self.map[p[0]][p[1]] = SparePart(i)
        for i in range(randint(0,15)):
            p = self.getEmptyLocation()
            self.map[p[0]][p[1]] = SparePart(Planet.PIECES_IMAGES[randint(0,4)])
        for i in range(randint(2, 5)):
            p = self.getEmptyLocation()
            self.map[p[0]][p[1]] = Portal(self, [p[0], p[1]])


        # If its not the starting planet
        # Setup a map for a planet that isn't the starting Planet
        # It has spare parts and wormholes
        

        # Examples of making all three items on a planet
        x = SparePart("./Img/screw.ppm") 
        y = ShipPiece("./Img/cabin.ppm", "working")

    def getEmptyLocation(self):
        """choses a random empty location on the map and returns it

        Returns:
            [int, int]: the location chosen as a coordinate [column, row]
        """
        # Optional method, but helpful for Part 1
        # Find an empty place in the map
        # Return its location as a list [row,col]
        l = []
        for i in range(len(self.map)):
            for j in range(len(self.map)):
                if not self.map[i][j]:
                    l.append([i, j])
        return l[randint(0, len(l)-1)]
    
    def isPortal(self, row, column):
        """Are these row, column coordinates a portal? Returns True/False. """
        return self.map[row][column] and self.map[row][column].getKind() == "portal"
    

    def getPortal(self, row, column) -> Portal:
        if self.map[row][column] and self.map[row][column].getKind() == "portal":
            return self.map[row][column]
        else:
            return None

    def findAPortal(self):
        """ Return the location [row,col] of some (unconnected) portal. """
        l = []
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.isPortal(i,j):
                    l.append([i,j])
        return l[randint(0, len(l)-1)]
    
    def setupWormhole(self, row, column):
        """ Make sure the wormhole is ready to go at coordinates [row,column] """
        if not self.isPortal(row, column):
            return -1
        p = self.getPortal(row, column)
        if p.isConnected():
            return 0
        pla = Planet()
        loc = pla.findAPortal()
        op = pla.getPortal(loc[0], loc[1])
        p.setOtherPortal(op)
        op.setOtherPortal(p)
        return 1



        

p = Planet()