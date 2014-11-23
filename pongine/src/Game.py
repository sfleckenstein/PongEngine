import pygame
import time
import sys

class Game:
    def __init__(self, Players, Arena, Balls, ball_colors):
        self.players = Players
        self.arena = Arena
        self.balls = Balls
        self.ball_colors = ball_colors
   
        self.background_color = (0, 0, 0)
        self.side_color = (255, 255, 255)

        pygame.init()
        self.window = pygame.display.set_mode((640,480))

    def render(self):
        while True:
            time.sleep(0.01)
            self.arena.render(self.window, self.side_color)
    
            for i in xrange(len(self.balls)):
                self.balls[i].render(self.window, self.background_color)
                self.balls[i].move(self.arena)
                self.balls[i].render(self.window, self.ball_colors[i])
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit(0)
     
