import unittest
from game import *

class testGame2(unittest.TestCase):
    def test_setup_wormhole(self):
        g = Game()
        c = g.planet.findAPortal()
        p = g.planet.getPortal(c[0], c[1])
        g._location = p.getLocation()
        g.planet.setupWormhole(g._location[0], g._location[1])
        self.assertEqual(p.getLocation(), g._location)
        self.assertEqual(p.getPlanet(), g.planet)
        self.assertIsInstance(p.getOtherPortal(), Portal)
    
    def test_unconnected_teleport(self):
        g = Game()
        c = g.planet.findAPortal()
        p = g.planet.getPortal(c[0], c[1])
        g._location = p.getLocation()
        pla = g.planet
        loc = g._location
        g.teleport()
        self.assertNotEqual(pla, g.planet)
        self.assertNotEqual(loc, g._location)

    def test_connected_teleport(self):
        g = Game()
        c = g.planet.findAPortal()
        p = g.planet.getPortal(c[0], c[1])
        g._location = p.getLocation()
        pla = g.planet
        loc = g._location
        g.teleport()
        g.teleport()
        self.assertEqual(pla, g.planet)
        self.assertEqual(loc, g._location)

    def test_show_way_back(self):
        g = Game()
        c = g.planet.findAPortal()
        p = g.planet.getPortal(c[0], c[1])
        g._location = p.getLocation()
        g.teleport()
        g.showWayBack()
        self.assertEqual(g.planet.getPortal(g._location[0], g._location[1])._imageName, "./Img/portal_flashing.ppm")

unittest.main()
