import unittest
from planet import Planet
from items import SparePart, ShipPiece, Portal

class TestPlanet(unittest.TestCase):
    def testInstanceFields(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify if the attributes are initialized as they should
        
        # TODO Part 1
        # Make a starting Planet
        p = Planet(15, True) 
        # Test the type of each instance field
        self.assertIsInstance(p.map, list)
        self.assertTrue(len(p.map) == len(p.map) and len(p.map) == 15)
    
    def testShipPieces(self):
        # The below fails so you remember to replace it with a real test
        
        # TODO Part 1
        # Make a starting Planet
        p = Planet(15, True)
        n = 0
        b = 0
        types = []
        for i in range(len(p.map)):
            for j in range(len(p.map[0])):
                if type(p.map[i][j]) is ShipPiece:
                    n+=1
                    if p.map[i][j].getImageName() not in types:
                        types.append(p.map[i][j].getImageName())
                    if "broken" in p.map[i][j].getImageName() and p.map[i][j].getStatus() == "broken":
                        b+=1
        self.assertEqual(5, n)
        self.assertGreaterEqual(b, 4)
        self.assertEqual(len(types), 3)

                    
                

        
    def testSpareParts(self):
        # The below fails so you remember to replace it with a real test
        
        # TODO Part 1
        # Make a starting Planet
        p = Planet(15, True)
        p1 = 0
        t = []
        for i in range(len(p.map)):
            for j in range(len(p.map[0])):
                if type(p.map[i][j]) is SparePart:
                    p1+=1
                    if p.map[i][j].getImageName() not in t:
                        t.append(p.map[i][j].getImageName())
        
        self.assertTrue(len(t) == 5)
        self.assertGreaterEqual(p1, 5)
        self.assertLessEqual(p1, 20)

        p = Planet(15, True)
        p2 = 0
        t = []
        for i in range(len(p.map)):
            for j in range(len(p.map[0])):
                if type(p.map[i][j]) is SparePart:
                    p2+=1
                    if p.map[i][j].getImageName() not in t:
                        t.append(p.map[i][j].getImageName())
        
        self.assertTrue(len(t) == 5)
        self.assertGreaterEqual(p2, 5)
        self.assertLessEqual(p2, 20)

        p = Planet(15, True)
        p3 = 0
        t = []
        for i in range(len(p.map)):
            for j in range(len(p.map[0])):
                if type(p.map[i][j]) is SparePart:
                    p3+=1
                    if p.map[i][j].getImageName() not in t:
                        t.append(p.map[i][j].getImageName())
        
        self.assertTrue(len(t) == 5)
        self.assertGreaterEqual(p3, 5)
        self.assertLessEqual(p3, 20)

        p = Planet(15, True)
        p4 = 0
        t = []
        for i in range(len(p.map)):
            for j in range(len(p.map[0])):
                if type(p.map[i][j]) is SparePart:
                    p4+=1
                    if p.map[i][j].getImageName() not in t:
                        t.append(p.map[i][j].getImageName())
        
        self.assertTrue(len(t) == 5)
        self.assertGreaterEqual(p4, 5)
        self.assertLessEqual(p4, 20)
        self.assertNotIn(p1, [p2, p3, p4])
        self.assertNotIn(p2, [p1, p3, p4])
        self.assertNotIn(p3, [p1, p2, p4])
        self.assertNotIn(p4, [p2, p3, p1])
        
    def testPortals(self):
        # The below fails so you remember to replace it with a real test
        
        # TODO Part 1
        # Make a starting Planet
        p = Planet(15, True)
        p1 = 0
        t = []
        for i in range(len(p.map)):
            for j in range(len(p.map[0])):
                if type(p.map[i][j]) is Portal:
                    p1+=1
                    
        self.assertGreaterEqual(p1, 2)
        self.assertLessEqual(p1, 5)

        p = Planet(15, True)
        p2 = 0
        t = []
        for i in range(len(p.map)):
            for j in range(len(p.map[0])):
                if type(p.map[i][j]) is Portal:
                    p2+=1
        
        self.assertGreaterEqual(p2, 2)
        self.assertLessEqual(p2, 5)

        p = Planet(15, True)
        p3 = 0
        t = []
        for i in range(len(p.map)):
            for j in range(len(p.map[0])):
                if type(p.map[i][j]) is Portal:
                    p3+=1
        
        self.assertGreaterEqual(p3, 2)
        self.assertLessEqual(p3, 5)

        self.assertNotIn(p1, [p2, p3])
        self.assertNotIn(p2, [p1, p3])
        self.assertNotIn(p3, [p1, p2])
        # Test the number of portals to make sure there are enough
        
        # Make second, third, and fourth starting Planets
        # Get the number of portals of each
        # Test that they do not all have the same number of portals.
        
    
if __name__ == '__main__':
    unittest.main()
