from Side import collision

class Arena:
    def __init__(self, sides):
        self.sides = sides
    
    def collision(self, arena, ball):
        for side in arena.sides:
            [is_collision, new_ball] = side.collision(ball)
            if is_collision:
                ball = new_ball

