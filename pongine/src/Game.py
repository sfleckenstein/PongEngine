import Tkinter

from Player import move_paddle

root = Tkinter.Tk()

class Game:
    def __init__(self, Players, Arena, Balls):
        self.Players = Players
        self.Arena = Arena
        self.Balls = Balls
    
    def motion(event):
        move_paddles(event.x, event.y)
