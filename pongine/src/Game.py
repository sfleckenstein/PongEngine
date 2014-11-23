import pygame
import time

class Game:
    def __init__(self, Players, Arena, Balls):
        self.players = Players
        self.arena = Arena
        self.balls = Balls
   
        self.background_color = (0, 0, 0)
        self.ball_color = (255, 255, 255)
        self.side_color = (255, 255, 255)

        pygame.init()
        self.window = pygame.display.set_mode((640,480))

    def render(self):
        self.arena.render(self.window, self.side_color)
        
        while True:
            time.sleep(0.01)
            
#            for ball in self.balls:    
            self.balls.render(self.window, self.background_color)
            self.balls.move(self.arena)
            self.balls.render(self.window, self.ball_color)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
 
