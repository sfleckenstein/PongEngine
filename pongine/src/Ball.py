import pygame

class Ball:
    def __init__(self, position, direction, speed, radius):
        self.position = position
        self.direction = direction
        self.speed = speed
        self.radius = radius
     
    def render(self, window, color):
        pygame.draw.circle(window, color, (self.position[0], self.position[1]), self.radius)

    def move(self):
        self.position[0] = self.position[0] + self.direction[0]
        self.position[1] = self.position[1] + self.direction[1]
    
