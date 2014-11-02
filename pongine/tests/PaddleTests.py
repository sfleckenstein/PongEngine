import unittest

from src.Side import Side
from src.Paddle import Paddle

class PaddleTests(unittest.TestCase):
    def setUp(self):
        self.horz_side = Side([0,0], [20,0], 1.0)

        self.paddle_room_to_move = Paddle(self.horz_side, 2, 5, 0)
        self.paddle_no_room_to_move_right = Paddle(self.horz_side, 2, 18, 0)
        self.paddle_no_room_to_move_left = Paddle(self.horz_side, 2, 2, 0)

    def test_successful_move_paddle_right(self):
        delta = 2
        old_x = self.paddle_room_to_move.x
        self.paddle_room_to_move.move_x(delta)
        self.assertEqual(self.paddle_room_to_move.x, old_x + delta)
    
    def test_successful_move_paddle_left(self):
        delta = -2
        old_x = self.paddle_room_to_move.x
        self.paddle_room_to_move.move_x(delta)
        self.assertEqual(self.paddle_room_to_move.x, old_x + delta)

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

if __name__ == "__main__":
     unittest.main()
