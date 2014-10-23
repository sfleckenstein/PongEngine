from Side import collision

class Arena:
    def __init__(self, sides):
        self.sides = sides
    
    def collision(self, arena, ball):
        for side in arena.sides:
            if side.collision(ball):
                return side

