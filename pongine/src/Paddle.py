class Paddle:
    def __init__(self, side, length):
        self.move_vector[0] = side.end[0] - side.start[0]
        self.move_vector[1] = side.end[1] - side.start[1]
        self.side = side
        self.length = length

    def move_x(self, delta):
        if self.move_vector[0] != 0:
            # TODO: verify that this is in bounds
            if self.room_to_move_x(delta):
                x = x + delta

    def move_y(self, delta):
        if self.move_vector[1] != 0:
            # TODO: verify that this is in bounds
            if self.room_to_move_y(delta):
                y = y + delta

    # TODO: figure out how to acutually determine this
    def room_to_move_x(self, delta):
        return True
    
    # TODO: figure out how to acutually determine this
    def room_to_move_y(self, delta):
        return True
