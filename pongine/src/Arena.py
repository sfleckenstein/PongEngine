
class Arena:
    def __init__(self, sides):
        self.sides = sides

        for i in xrange(len(sides)):
            next_index = (i + 1) % len(sides)
            sides[i].set_normal(sides[next_index])
    
    def collision(self, arena, ball):
        for side in arena.sides:
            [is_collision, new_ball] = side.collision(ball)
            if is_collision:
                ball = new_ball

