import pygame
import sys
import time

from src.Ball import Ball

class BallRenderTests():
    def setUp(self):
        self.ball = Ball([200, 200], [1, 0], 5, 7)
        self.background_color = (0, 0, 0)
        self.ball_color = (255, 255, 255)
 
    def test(self):
        pygame.init()
        window = pygame.display.set_mode((640,480))
    
        while True:
            time.sleep(0.01)
            self.ball.render(window, self.background_color)
            self.ball.move()
            self.ball.render(window, self.ball_color)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

if __name__ == "__main__":
    blah = BallRenderTests()
    blah.setUp()  
    blah.test()
