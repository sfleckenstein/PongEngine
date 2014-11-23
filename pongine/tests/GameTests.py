import pygame
import sys

from src.Game import Game
from src.Arena import Arena
from src.Side import Side
from src.Ball import Ball

class GameTests():
    def setUp(self):
        side0 = Side((10,10), (10,400), 1.0)
        side1 = Side((10,400), (400,400), 1.0)
        side2 = Side((400,400), (400,10), 1.0)
        side3 = Side((400,10), (10,10), 1.0)
        self.arena = Arena((side0, side1, side2, side3))
        
        self.ball0 = Ball([250, 200], [1, 1], 3, 10)
        self.ball1 = Ball([200, 250], [1, -1], 2, 10)
        self.background_color = (0, 0, 0)
        self.ball0_color = (51, 255, 204)
        self.ball1_color = (204, 255, 51)
       
        self.game = Game((), self.arena, (self.ball0, self.ball1), (self.ball0_color, self.ball1_color))

    def run(self):
        self.game.render()

if __name__ == "__main__":
    game_test = GameTests()
    game_test.setUp()
    game_test.run() 
 
