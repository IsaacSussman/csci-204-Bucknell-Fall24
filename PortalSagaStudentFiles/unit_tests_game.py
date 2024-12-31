import unittest
from game import Game
from planet import Planet
from items import *

class TestGame(unittest.TestCase):
    def testInit(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify if the attributes are initialized as they should
        
        # TODO Part 1
        # Make a Game (don't call start())
        # Test that the instance fields are the correct types
        g = Game()
        self.assertIsInstance(g.planet, Planet)
        self.assertIsInstance(g._location, list)
        self.assertTrue(len(g.planet.map) == len(g.planet.map) and len(g.planet.map) == Game.SIZE)
        self.assertIsNone(g.getImage(g.getRoverLocation()))

    def testGoUp(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        
        # TODO Part 1
        # Make a Game
        # Set the rover location to a location of your choosing
        g = Game()
        g.planet.map[1][1] = None if type(g.planet.map[1][1]) == Portal else g.planet.map[1][1]
        print("Empty" if g.planet.map[1][1] is None else "Full")
        g._location = [1, 1]
        g.goUp()
        self.assertTrue(g._location == [0,1])
        
    def testGoDown(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        
        # TODO Part 1
        # This is the same idea as goUp
        g = Game()
        g.planet.map[1][1] = None if type(g.planet.map[1][1]) == Portal else g.planet.map[1][1]
        g._location = [1, 1]
        g.goDown()
        self.assertTrue(g._location == [2,1])
        
    def testGoLeft(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        
        # TODO Part 1
        # This is the same idea as goUp
        g = Game()
        g.planet.map[1][1] = None if type(g.planet.map[1][1]) == Portal else g.planet.map[1][1]
        g._location = [1, 1]
        g.goLeft()
        self.assertTrue(g._location == [1,0])
        
    def testGoRight(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        
        # TODO Part 1
        # This is the same idea as goUp
        g = Game()
        g.planet.map[1][1] = None if type(g.planet.map[1][1]) == Portal else g.planet.map[1][1]
        g._location = [1, 1]
        g.goRight()
        self.assertTrue(g._location == [1,2])
        
    def testShowWayBack(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        
        # TODO Part 2
        self.assertTrue(False)
        
    def testPickUp(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        
        # TODO Part 3
        self.assertTrue(False)
        
    def testPerformTask(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        
        # TODO Part 3
        self.assertTrue(False)
        
    # add more test functions for other methods you have added (except simple gettter and setters methods)
    
if __name__ == '__main__':
    unittest.main()
    
