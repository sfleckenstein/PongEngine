from math import sqrt, pow

class Side:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
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
            return False
       
        return True
       
#        x_plus  = self.intersection_x_plus(dx, dy, dr, det, ball.radius)        
#        x_minus = self.intersection_x_minus(dx, dy, dr, det, ball.radius)        
#        y_plus  = self.intersection_y_plus(dx, dy, dr, det, ball.radius)        
#        y_minus = self.intersection_y_minus(dx, dy, dr, det, ball.radius)        
#
#        print x_plus
#        print x_minus
#        print y_plus
#        print y_minus
#
#        if (x_plus is None and x_minus is None) or (y_plus is None and y_minus is None):
#           return False
#
#        return True 
#
#    def intersection_x_plus(self, dx, dy, dr, det, rad):
#        try:
#            return (det*dy + self.sign(dy)*dx*sqrt(pow(rad,2)*pow(dr,2) - pow(det, 2)))/pow(dr, 2) 
#        except ValueError:
#            return None 
#
#    def intersection_x_minus(self, dx, dy, dr, det, rad):
#        try:
#            return (det*dy - self.sign(dy)*dx*sqrt(pow(rad,2)*pow(dr,2) - pow(det, 2)))/pow(dr, 2)
#        except ValueError:
#            return None 
#
#    def intersection_y_plus(self, dx, dy, dr, det, rad):
#        try:
#            return (-det * dx + abs(dy) * sqrt(pow(rad, 2) * pow(dr, 2) - pow(det, 2)))/ pow(dr, 2)
#        except ValueError:
#            return None 
#    
#    def intersection_y_minus(self, dx, dy, dr, det, rad):
#        try:
#            return (-det * dx - abs(dy) * sqrt(pow(rad, 2) * pow(dr, 2) - pow(det, 2)))/ pow(dr, 2) 
#        except ValueError:
#            return None
#
#    def sign(self, value):
#        if value < 0:
#            return -1
#        return 1
#
