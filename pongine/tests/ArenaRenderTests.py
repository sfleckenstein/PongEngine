import pygame
import sys

from src.Side import Side
from src.Arena import Arena

class ArenaRenderTests():
    def setUp(self):
        side0 = Side((10,10), (10,400), 1.0)
        side1 = Side((10,400), (400,400), 1.0)
        side2 = Side((400,400), (400,10), 1.0)
        side3 = Side((400,10), (10,10), 1.0)
        self.arena = Arena((side0, side1, side2, side3))

    def test(self):
        pygame.init()
        window = pygame.display.set_mode((640,480))
        self.arena.render(window, (255, 255, 255))
        pygame.display.flip()       
 
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)


if __name__ == "__main__":
    blah = ArenaRenderTests()
    blah.setUp()  
    blah.test()

