class Arena:
    def __init__(self, sides):
        # The angles between sides must be in: [45, 90] in
        # order to make sure that the paddle motion is reliable
        self.sides = sides

        # The calculations for side normals use the potential
        # normals of a neighbor to determine which potential
        # normal is the interior one (the one we want)
        for i in xrange(len(sides)):
            next_index = (i + 1) % len(sides)
            sides[i].set_normal(sides[next_index])
    
    def collision(self, ball):
        for side in self.sides:
            [is_collision, new_ball] = side.collision(ball)
            if is_collision:
                ball.direction = new_ball.direction
                ball.speed = new_ball.speed
    
    def render(self, window, color):
        for side in self.sides:
            side.render(window, color)

