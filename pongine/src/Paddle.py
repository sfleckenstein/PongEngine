class Paddle:
    def __init__(self, side, length, x, y):
#        self.move_vector[0] = side.end[0] - side.start[0]
#        self.move_vector[1] = side.end[1] - side.start[1]
        self.side = side
        self.length = length
        self.x = x
        self.y = y 

    def move_x(self, delta):
        if self.move_vector[0] != 0:
            if self.room_to_move_x(delta):
                x = x + delta

    def move_y(self, delta):
        if self.move_vector[1] != 0:
            if self.room_to_move_y(delta):
                y = y + delta

    def room_to_move_x(self, delta):
        # We are moving to the right
        if delta > 0:
            # The start of the side is to the left of the end
            if self.side.start[0] < self.side.end[0]:
	            if self.x + delta + self.length/2 < self.end[0]:
	                return True
            # The start of the side is to the right of the end
            else:
                if self.x + delta + self.length/2 < self.start[0]:
                    return True
        # We are moving to the left
        else:
            # The start of the side is on the left of the end
            if self.side.start[0] < self.side.end[0]:
                if self.x + delta - self.length/2 > self.start[0]:
                    return True
            # The start of the side is on the right of the end
            else:
                if self.x + delta - self.length/2 > self.end[0]:
                    return True
        return False
 
    def room_to_move_y(self, delta):
        # We are moving up
        if delta > 0:
            # The start of the side is below the end
            if self.side.start[1] < self.side.end[1]:
                if self.y + delta + self.length/2 < self.side.end[1]:
                    return True
            # The start of the side is above the end
            else:
                if self.y + delta + self.length/2 < self.side.start[1]:
                    return True
        # We are moving down
        else:
            # The start of the side is below the end
            if self.side.start[1] < self.side.end[1]:
                if self.y + delta - self.length/2 > self.side.start[1]:
                    return True
            # The start of the side is above the end
            else:
                if self.y + delta - side.length/2 > self.side.end[1]:
                    return True
        return False
                 
