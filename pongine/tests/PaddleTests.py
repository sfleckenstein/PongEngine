import unittest

from src.Side import Side
from src.Paddle import Paddle

class PaddleTests(unittest.TestCase):
    def setUp(self):
        self.horz_side = Side([0,0], [20,0], 1.0)
        self.vert_side = Side([0,0], [0,20], 1.0)

        self.paddle_room_to_move_horz = Paddle(self.horz_side, 2, 5, 0)
        self.paddle_no_room_to_move_right = Paddle(self.horz_side, 2, 18, 0)
        self.paddle_no_room_to_move_left = Paddle(self.horz_side, 2, 2, 0)

        self.paddle_room_to_move_vert = Paddle(self.vert_side, 2, 0, 10)
        self.paddle_no_room_to_move_up = Paddle(self.vert_side, 2, 0, 18)
        self.paddle_no_room_to_move_down = Paddle(self.vert_side, 2, 0, 2)

    def test_successful_move_paddle_right(self):
        delta = 2
        old_x = self.paddle_room_to_move_horz.x
        self.paddle_room_to_move_horz.move_x(delta)
        self.assertEqual(self.paddle_room_to_move_horz.x, old_x + delta)
    
    def test_successful_move_paddle_left(self):
        delta = -2
        old_x = self.paddle_room_to_move_horz.x
        self.paddle_room_to_move_horz.move_x(delta)
        self.assertEqual(self.paddle_room_to_move_horz.x, old_x + delta)

    def test_failed_move_paddle_right(self):
        delta = 2
        old_x = self.paddle_no_room_to_move_right.x
        self.paddle_no_room_to_move_right.move_x(delta)
        self.assertEqual(self.paddle_no_room_to_move_right.x, old_x)

    def test_failed_move_paddle_left(self):
        delta = -2
        old_x = self.paddle_no_room_to_move_left.x
        self.paddle_no_room_to_move_left.move_x(delta)
        self.assertEqual(self.paddle_no_room_to_move_left.x, old_x)
       
    def test_successful_move_paddle_up(self):
        delta = 2
        old_y = self.paddle_room_to_move_vert.y
        self.paddle_room_to_move_vert.move_y(delta)
        self.assertEqual(self.paddle_room_to_move_vert.y, old_y + delta) 
    
    def test_successful_move_paddle_down(self):
        delta = -2
        old_y = self.paddle_room_to_move_vert.y
        self.paddle_room_to_move_vert.move_y(delta)
        self.assertEqual(self.paddle_room_to_move_vert.y, old_y + delta) 

    def test_failed_move_paddle_up(self):
        delta = 2
        old_y = self.paddle_no_room_to_move_up.y
        self.paddle_no_room_to_move_up.move_y(delta)
        self.assertEqual(self.paddle_no_room_to_move_up.y, old_y) 
        
    def test_failed_move_paddle_down(self):
        delta = -2
        old_y = self.paddle_no_room_to_move_down.y
        self.paddle_no_room_to_move_down.move_y(delta)
        self.assertEqual(self.paddle_no_room_to_move_down.y, old_y) 

    # TODO: add tests for room_to_move_x and room_to_move_y
 
if __name__ == "__main__":
     unittest.main()
