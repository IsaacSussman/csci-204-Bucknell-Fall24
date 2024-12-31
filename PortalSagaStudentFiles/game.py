from GUI.graphics import Point
from items import SparePart, ShipPiece, Portal
from planet import Planet
from stack import *   
from mylist import MyList   
from myqueue import LinkedQueue   
from task import Task
import random
    

class Game:
    SIZE = 15                 # 15x15 squares in the map

    def __init__(self):
        # TODO Part 1
        # Your game needs instance fields for:
        # 1) a Planet instance. This is the current planet you are on. 
        #      It begins as a starting planet.
        # 2) a rover location of row and column. This is where you are 
        #       on the map.  The rover starts in an empty location on the map.
        self.planet = Planet(Game.SIZE, True)
        self._location = self.planet.getEmptyLocation()
        self.stack = LinkedStack()
        self.inventory = MyList()
        self.tasks = LinkedQueue()

        for i in ["cabin", "exhaust", "exhaust", "engine", "engine"]:
            t = Task(i)
            PIECES_IMAGES = ["screw", "gear", "lettuce", "bagel", "cake"]
            for j in range(random.randint(2, 4)):
                pi = random.randint(0,len(PIECES_IMAGES)-1)
                t.addComponent(random.randint(1,5), PIECES_IMAGES[pi])
                PIECES_IMAGES.pop(pi)
            self.tasks.enqueue(t)
        self.fixed = 0



        # TODO Part 2
        # Your game needs instance fields for:
        # 1) a Stack of Portals the rover has traveled through

        # TODO Part 3
        # Your game needs instance fields for:
        # 1) a List of items in your inventory
        # 2) a Queue of tasks to fix the broken ship pieces
        pass

    def getRoverImage(self):
        """ Called by GUI when screen updates.
            Returns image name (as a string) of the rover. 
		(Likely './Img/rover.ppm') """
        # Only edit this if you get your own rover image
        return './Img/rover.ppm'

    def getRoverLocation(self):
        """ Called by GUI when screen updates.
            Returns location (as a Point). """
        # TODO Part 1
        # return Point(column, row) # backwards of what you expect
        pass 
        return Point(self._location[1],self._location[0])

    def getImage(self, point):
        """ Called by GUI when screen updates.
            Returns image name (as a string) or None for the 
		    spare part, ship component, or portal at the given 
		    point coordinates. (such as './Img/engine.ppm') """
        row = point.y # point is backwards of what you expect
        col = point.x
        # TODO Part 1
        if self.planet.map[row][col]:
            return self.planet.map[row][col].getImageName()
        else:
            return None

    def teleport(self):
        if self.planet.isPortal(self._location[0], self._location[1]):
            
            
            self.planet.setupWormhole(self._location[0], self._location[1])
            p = self.planet.getPortal(self._location[0], self._location[1]).getOtherPortal()
            p._imageName = "./Img/portal.ppm"
            if (self.stack.peek() if not self.stack.peek() else self.stack.peek().hash) == p.hash:
                self.stack.pop()
            else:
                self.stack.push(p.getOtherPortal())
            self.planet = p.planet
            self._location = p.location


    def goUp(self):
        """ Called by GUI when button clicked.
            If legal, moves rover. If the robot lands
            on a portal, it will teleport. """
        if self._location[0] == 0:
            self._location[0] = len(self.planet.map)-1
        else:
            self._location[0]-=1
        if self.planet.isPortal(self._location[0], self._location[1]):
            self.teleport()
            

    def goDown(self):
        """ Called by GUI when button clicked. 
            If legal, moves rover. If the robot lands
            on a portal, it will teleport. """
        if self._location[0] == len(self.planet.map)-1:
            self._location[0] = 0
        else:
            self._location[0]+=1
        if self.planet.isPortal(self._location[0], self._location[1]):
            self.teleport()
        # TODO Part 2
        # If the robot lands on a portal, teleport

    def goLeft(self):
        """ Called by GUI when button clicked. 
            If legal, moves rover. If the robot lands
            on a portal, it will teleport. """
        if self._location[1] == 0:
            self._location[1] = len(self.planet.map)-1
        else:
            self._location[1]-=1

        if self.planet.isPortal(self._location[0], self._location[1]):
            self.teleport()
        # If the robot lands on a portal, teleport

    def goRight(self):
        """ Called by GUI when button clicked. 
            If legal, moves rover. If the robot lands
            on a portal, it will teleport. """
        if self._location[1] == len(self.planet.map)-1:
            self._location[1] = 0
        else:
            self._location[1]+=1

        if self.planet.isPortal(self._location[0], self._location[1]):
            self.teleport()
        # If the robot lands on a portal, teleport

    def showWayBack(self):
        """ Called by GUI when button clicked.
            Flash the portal leading towards home. """
        # TODO Part 2
        if not self.stack.peek():
            return
        self.stack.peek().getOtherPortal()._imageName = "./Img/portal_flashing.ppm"

    def getInventory(self):
        """ Called by GUI when inventory updates.
            Returns entire inventory (as a string). 
		3 cake
		2 screws
		1 rug
	  """
        # TODO Part 3
        pass 

    def pickUp(self):
        """ Called by GUI when button clicked. 
		If rover is standing on a part (not a portal 
		or ship component), pick it up and add it
		to the inventory. """
        # TODO Part 3
        pass 

    def getCurrentTask(self):
        """ Called by GUI when task updates.
            Returns top task (as a string). 
		'Fix the engine using 2 cake, 3 rugs' or
		'You win!' 
 	  """
        # TODO Part 3
        pass 

    def performTask(self):
        """ Called by the GUI when button clicked.
            If necessary parts are in inventory, and rover
            is on the relevant broken ship piece, then fixes
            ship piece and removes parts from inventory. If
            we run out of tasks, we win. """
        # TODO Part 3
        pass 

    # Put other methods here as needed if nay.
    def setRoverLocation(self, row, col):
        """sets rover's location to [row, col]"""
        self._location = [row, col]

    def pickUp(self):
        if self.planet.map[self._location[0]][self._location[1]] and self.planet.map[self._location[0]][self._location[1]].getKind() == "part":
            self.inventory.insert(self.planet.map[self._location[0]][self._location[1]].getName(),0)
            self.planet.map[self._location[0]][self._location[1]] = None

    def getInventory(self):
        s = ""
        for i in ["screw", "gear", "lettuce", "bagel", "cake"]:
            s += (("\n" if i != "screw" else "") + (str(self.inventory.count(i))+" "+i)) if self.inventory.count(i) != 0 else ""
        return s
    
    def getCurrentTask(self):
        if self.fixed >= 5:
            return "You Win!"
        t = self.tasks.peek()
        n = t.getName()
        c = t.getComponents()
        return "Fix the "+n+" using "+", ".join([f"{c[x]} {x}" for x in c.keys()])+"."
    
    def performTask(self):
        t = self.tasks.peek()
        n = t.getName()
        c = t.getComponents()
        i = self.planet.map[self._location[0]][self._location[1]]
        if type(i) is ShipPiece and i.getStatus() == "broken" and n == i.getName():
            for j in c:
                if not self.inventory.count(j) >= c[j]:
                    return
            i.setStatus("working")
            for j in c:
                for k in range(c[j]):
                    self.inventory.remove(j)
            self.tasks.dequeue()
            self.fixed+=1
            print(self.tasks, self.tasks.peek())

    
    
