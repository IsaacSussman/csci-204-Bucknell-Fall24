import unittest
from io import StringIO
import sys

from project1_solution import Cave, Adventure

class TestMove2(unittest.TestCase):
    TEST_CAVE_2_LAYOUT = [ 
        ["R", "R", "R", "R", "R"],
        ["R", "R", "_", "R", "R"],
        ["R", "S", "_", "E", "R"],
        ["R", "R", "_", "R", "R"],
        ["R", "R", "R", "R", "R"]
    ]

    def setup_cave_2():
        cave_2 = Cave("")
        cave_2.layout = TestMove2.TEST_CAVE_2_LAYOUT
        adv = Adventure(cave_2)
        return cave_2, adv

    def test_setup_2(self):
        cave_2, adv_2 = TestMove2.setup_cave_2()
        self.assertEqual(adv_2.current_spot,[2, 1])
        self.assertEqual(adv_2.visited,[[0,0,0,0,0],[1, 1, 1, 0, 0,],[1, 1, 1, 0, 0,],[1,1,1,0,0],[0,0,0,0,0]])
        self.assertEqual(adv_2.cave.layout,TestMove2.TEST_CAVE_2_LAYOUT)

    ## Test Can Move
    def test_can_move_down_2(self):
        cave_2, adv_2 = TestMove2.setup_cave_2()
        valid_move = adv_2.can_move("down")
        self.assertFalse(valid_move, "Cannot move "+
                         "down"+" in cave 2")

    def test_can_move_up_2(self):
        direction = "up"
        cave_2, adv_2 = TestMove2.setup_cave_2()
        valid_move = adv_2.can_move(direction)
        self.assertFalse(valid_move, "Cannot move "+
                         direction+" in cave 2")

    def test_can_move_left_2(self):
        direction = "left"
        cave_2, adv_2 = TestMove2.setup_cave_2()
        valid_move = adv_2.can_move(direction)
        self.assertFalse(valid_move, 
                         "Cannot move "+direction+ " in cave 2")

    def test_can_move_right_2(self):
            direction = "right"
            cave_2, adv_2 = TestMove2.setup_cave_2()
            valid_move = adv_2.can_move(direction)
            # if was anything other than bool, would also want to
            # check type
            self.assertTrue(valid_move, 
                            "Can move "+direction+ " in cave 2")

    ## Test Move
    # only test moving down, all other moves invalid
    def test_move_right_2(self):
        cave_2, adv_2 = TestMove2.setup_cave_2()
        adv_2.move("right")
        self.assertEqual(adv_2.current_spot, [2,2])
        self.assertEqual(adv_2.visited, [[0,0,0,0,0],[1, 1, 1, 1, 0,],[1, 1, 1, 1, 0,],[1,1,1,1,0],[0,0,0,0,0]])
        self.assertEqual(adv_2.cave.layout,TestMove2.TEST_CAVE_2_LAYOUT)
    
    def test_move_up_2(self):
        cave_2, adv_2 = TestMove2.setup_cave_2()
        adv_2.move("right")
        adv_2.move("up")
        self.assertEqual(adv_2.current_spot, [1,2])
        self.assertEqual(adv_2.visited, [[0,1,1,1,0],[1, 1, 1, 1, 0,],[1, 1, 1, 1, 0,],[1,1,1,1,0],[0,0,0,0,0]])
        self.assertEqual(adv_2.cave.layout,TestMove2.TEST_CAVE_2_LAYOUT)
    
    def test_move_down_2(self):
        cave_2, adv_2 = TestMove2.setup_cave_2()
        adv_2.move("right")
        adv_2.move("up")
        adv_2.move("down")
        adv_2.move("down")
        self.assertEqual(adv_2.current_spot, [3,2])
        self.assertEqual(adv_2.visited, [[0,1,1,1,0],[1, 1, 1, 1, 0,],[1, 1, 1, 1, 0,],[1,1,1,1,0],[0,1,1,1,0]])
        self.assertEqual(adv_2.cave.layout,TestMove2.TEST_CAVE_2_LAYOUT)
    
    def test_move_left_2(self):
        cave_2, adv_2 = TestMove2.setup_cave_2()
        adv_2.move("right")
        adv_2.move("up")
        adv_2.move("down")
        adv_2.move("down")
        adv_2.move("up")
        adv_2.move("left")
        self.assertEqual(adv_2.current_spot, [2,1])
        self.assertEqual(adv_2.visited, [[0,1,1,1,0],[1, 1, 1, 1, 0,],[1, 1, 1, 1, 0,],[1,1,1,1,0],[0,1,1,1,0]])
        self.assertEqual(adv_2.cave.layout,TestMove2.TEST_CAVE_2_LAYOUT)
    
    def test_move_to_finish_2(self):
        cave_2, adv_2 = TestMove2.setup_cave_2()
        adv_2.move("right")
        adv_2.move("up")
        adv_2.move("down")
        adv_2.move("down")
        adv_2.move("up")
        adv_2.move("left")
        adv_2.move("right")
        adv_2.move("right")
        self.assertEqual(adv_2.current_spot, [2,3])
        self.assertEqual(adv_2.visited, [[0,1,1,1,0],[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[1,1,1,1,1],[0,1,1,1,0]])
        self.assertEqual(adv_2.cave.layout,TestMove2.TEST_CAVE_2_LAYOUT)
     
    

     


unittest.main()