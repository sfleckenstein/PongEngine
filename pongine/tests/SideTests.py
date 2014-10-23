import unittest

from src.Side import Side
from src.Ball import Ball

class SideTests(unittest.TestCase):

    def setUp(self):
        self.side = Side([0, 0], [0, 2])
        self.ball_col = Ball([1, 1], [0, 0], 0, 1)
        self.ball_no_col = Ball([10, 10], [0, 0], 0, 1)
        self.ball_in_side = Ball([0, 1], [0, 0], 0, 1)

    def test_collision(self):
       self.assertTrue(self.side.collision(self.ball_col))

    def test_no_collision(self):
       self.assertFalse(self.side.collision(self.ball_no_col)) 
   
    def test_ball_in_side(self):
       self.assertTrue(self.side.collision(self.ball_in_side))
 
if __name__ == "__main__":
     unittest.main()
