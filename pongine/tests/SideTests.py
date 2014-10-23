import unittest

from src.Side import Side
from src.Ball import Ball

class SideTests(unittest.TestCase):

    def setUp(self):
        self.side = Side([0, 0], [0, 2], 1.0)
        self.faster_side = Side([0, 0], [0, 2], 1.5)
        self.slower_side = Side([0, 0], [0, 2], 0.5)
        self.side_45_col = Side([0, 0], [2, 0], 1.0)        

        self.ball_col = Ball([1, 1], [0, 0], 0, 1)
        self.ball_no_col = Ball([10, 10], [0, 0], 0, 1)
        self.ball_in_side = Ball([0, 1], [0, 0], 0, 1)
        self.ball_perp_col = Ball([1, 1], [-1, 0], 1, 1)
        self.ball_45_col = Ball([0, 1], [1, -1], 1, 1)

    def test_collision(self):
        [is_collision, new_ball] = self.side.collision(self.ball_col)
        self.assertTrue(is_collision)

    def test_no_collision(self):
        [is_collision, new_ball] = self.side.collision(self.ball_no_col)
        self.assertFalse(is_collision) 
   
    def test_ball_in_side(self):
        [is_collision, new_ball] = self.side.collision(self.ball_in_side)
        self.assertTrue(is_collision)

    def test_ball_position_with_collision(self):
        [is_collision, new_ball] = self.side.collision(self.ball_col)
        self.assertEqual(new_ball.position, self.ball_col.position)

    def test_ball_position_no_collision(self):
        [is_collision, new_ball] = self.side.collision(self.ball_no_col)
        self.assertEqual(new_ball.position, self.ball_no_col.position)

    def test_faster_ball_speed_with_collision(self):
        [is_collision, new_ball] = self.faster_side.collision(self.ball_col)
        self.assertEqual(new_ball.speed, self.ball_col.speed*1.5)
    
    def test_slower_ball_speed_with_collision(self):
        [is_collision, new_ball] = self.slower_side.collision(self.ball_col)
        self.assertEqual(new_ball.speed, self.ball_col.speed*0.5)

    def test_equal_ball_speed_with_collision(self):
        [is_collision, new_ball] = self.side.collision(self.ball_col)
        self.assertEqual(new_ball.speed, self.ball_col.speed)
        
    def test_ball_direction_with_perp_collision(self):
        [is_collision, new_ball] = self.side.collision(self.ball_perp_col)
        self.assertEqual(new_ball.direction[0], -self.ball_perp_col.direction[0])
        self.assertEqual(new_ball.direction[1], self.ball_perp_col.direction[1])

    def test_ball_direction_with_45_degree_collision(self):
        [is_collision, new_ball] = self.side.collision(self.ball_45_col)
        self.assertEqual(new_ball.direction, [1, 1])

if __name__ == "__main__":
     unittest.main()
