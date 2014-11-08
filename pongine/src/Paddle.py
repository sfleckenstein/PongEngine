class Paddle:
    def __init__(self, side, length, x, y):
        self.move_vector = [side.end[0] - side.start[0], side.end[1] - side.start[1]]
        self.side = side
        self.length = length
        self.x = x
        self.y = y 

    def move_x(self, delta):
        if self.move_vector[0] != 0:
            if self.room_to_move_x(delta):
                self.x = self.x + delta

    def move_y(self, delta):
        if self.move_vector[1] != 0:
            if self.room_to_move_y(delta):
                self.y = self.y + delta

    def room_to_move_x(self, delta):
        # We are moving to the right
        if delta > 0:
            # The start of the side is to the left of the end
            if self.side.start[0] < self.side.end[0]:
                if self.x + self.get_x_dist(delta) < self.side.end[0]:
	                return True
            # The start of the side is to the right of the end
            else:
                if self.x + self.get_x_dist(delta) < self.side.start[0]:
                    return True
        # We are moving to the left
        else:
            # The start of the side is on the left of the end
            if self.side.start[0] < self.side.end[0]:
                if self.x + self.get_x_dist(delta) > self.side.start[0]:
                    return True
            # The start of the side is on the right of the end
            else:
                if self.x + self.get_x_dist(delta) > self.side.end[0]:
                    return True
        return False
 
    def room_to_move_y(self, delta):
        # We are moving up
        if delta > 0:
            # The start of the side is below the end
            if self.side.start[1] < self.side.end[1]:
                if self.y + self.get_y_dist(delta) < self.side.end[1]:
                    return True
            # The start of the side is above the end
            else:
                if self.y + self.get_y_dist(delta) < self.side.start[1]:
                    return True
        # We are moving down
        else:
            # The start of the side is below the end
            if self.side.start[1] < self.side.end[1]:
                if self.y + self.get_y_dist(delta) > self.side.start[1]:
                    return True
            # The start of the side is above the end
            else:
                if self.y + self.get_y_dist(delta) > self.side.end[1]:
                    return True
        return False
              
    # The ratio of move_vector[0]/length is equal to the ratio of
    # the distance we are moving in the x direction/delta 
    def get_x_dist(self, delta):
        return (self.move_vector[0] * delta) / self.side.length 
    
    # The ratio of move_vector[1]/length is equal to the ratio of
    # the distance we are moving in the y direction/delta 
    def get_y_dist(self, delta):
        return (self.move_vector[1] * delta) / self.side.length
