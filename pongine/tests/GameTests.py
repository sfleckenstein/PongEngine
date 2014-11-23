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
        
        self.ball = Ball([250, 200], [1, 1], 5, 7)
        self.background_color = (0, 0, 0)
        self.ball_color = (255, 255, 255)
       
        self.game = Game((), self.arena, (self.ball))

    def run(self):
        self.game.render()

if __name__ == "__main__":
    game_test = GameTests()
    game_test.setUp()
    game_test.run() 
 
