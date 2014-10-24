from math import sqrt, pow

from Ball import Ball

class Side:
    def __init__(self, start, end, next_start, next_end, speed_attenuation):
        self.start = start
        self.end = end

        # This allows the ball to be sped up, or slowed
        # down when it hits a side.
        # This is a multiplicitive factor, so values
        # greater than 1 speed the ball up and values
        # less than 1 slow the ball down.
        self.speed_attenuation = speed_attenuation
        
        dx = end[0] - start[0]
        dy = end[1] - start[1]

        normal0 = [-dy, dx]
        normal1 = [dy, -dx]

        # This next chunk is used to determine which normal
        # points towards the interior of the arena. This is
        # necessary because if we use the exterior normal,
        # we get wonky bounces.        

        dx_next = next_end[0] - next_start[0]
        dy_next = next_end[1] - next_start[1]

        normal0_next = [-dy_next, dx_next]
        normal1_next = [dy_next, -dx_next]
        
        # If we don't start the normal from the center of its side,
        # it could miss the next_normal in the intersection detection
        normal_start = [(end[0] - start[1])/2, (end[1] - start[1])/2] 
        normal_next_start = [(next_end[0] - next_start[0])/2, (next_end[1] - next_start[1])]

        if self.get_interior_normal(normal0, normal_start, normal0_next, normal_next_start) or self.get_interior_normal(normal0, normal_start, normal1_next, normal_next_start):
            self.normal = normal0
        elif self.get_interior_normal(normal1, normal_start, normal0_next, normal_next_start) or self.get_interior_normal(normal1, normal_start, normal1_next, normal_next_start):
            self.normal = normal1
        else:
            # TODO: create own exception class for this
            raise Exception("No interior normal found")

    def collision(self, ball):
        """Detects of a collision has occured between a side and a ball"""
        # Algorithm from http://mathworld.wolfram.com/Circle-LineIntersection.html
        
        # First, normalize the coordinates so the ball is at (0,0)
        # (x1, y1)
        side_start = [self.start[0] - ball.position[0],
                     self.start[1] - ball.position[1]]

        # (x2, y2)
        side_end = [self.end[0] - ball.position[0],
                    self.end[1] - ball.position[1]]
        
        dx = side_end[0] - side_start[0]
        dy = side_end[1] - side_start[1]
        dr = sqrt(pow(dx, 2) + pow(dy, 2))
        
        det = side_start[0]*side_end[1] - side_start[1]*side_end[0]

        discriminant = pow(ball.radius, 2) * pow(dr, 2) - pow(det, 2)

        if discriminant < 0:
            return [False, ball]  
       
        return [True, self.get_new_ball_params(ball)]
       
    # This is invoked after a collision with a side
    # to determine the ball's direction and speed.
    # Algorithm from http://math.stackexchange.com/questions/13261/how-to-get-a-reflection-vector
    def get_new_ball_params(self, ball):
        # Speed up or slow the ball down
        new_speed = self.speed_attenuation * ball.speed

        two_d = 2 * ball.direction
        two_d_dot_n = two_d[0] * self.normal[0] + two_d[1] * self.normal[1]
        
        magnitude_n_squared = self.normal[0] * self.normal[0] + self.normal[1] * self.normal[1]

        r_x = ball.direction[0] - (two_d_dot_n / magnitude_n_squared) * self.normal[0]
        r_y = ball.direction[1] - (two_d_dot_n / magnitude_n_squared) * self.normal[1]

        return Ball(ball.position, [r_x, r_y], new_speed, ball.radius)

    # Checks to see which pair of normals intersect. The only rays that intersect will be 
    # the two interior normals.
    # Alorithm from Gunter Blache's answer to http://stackoverflow.com/questions/2931573/determining-if-two-rays-intersect 
    def get_interior_normal(self, normal, normal_start, normal_next, normal_next_start):
        dx = normal_next_start[0] - normal_start[0]
        dy = normal_next_start[1] - normal_start[1]

        det = normal_next[0] * normal[1] - normal_next[1] * normal[0]

        u = ((dy * normal_next[0] - dx * normal_next[1]) * det) < 0
        v = ((dy * normal[0] - dx * normal[1]) * det) < 0

        return (u and v)
