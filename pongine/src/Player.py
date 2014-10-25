class Player:
    def __init__(self, paddles):
        self.paddles = paddles

        # TODO: this could cause strange paddle behavior
        # before the mouse moves the first time
        self.mouse_x = 0
        self.mouse_y = 0

    # This assumes that all of the paddles move together
    # and are controlled by the mouse.
    def move_paddles(self, new_x, new_y):
        # TODO: this assumes that only one of x or y can change
        # at a time. VERIFY
        for paddle in self.paddles:
            if new_x != self.mouse_x:
                # TODO: verify that these x and y changes work
                # as the player would expect
                move_x(paddle, new_x - self.mouse_x)
            else:
                move_y(paddle, new_y - self.mouse_y)
        self.mouse_x = new_x
        self.mouse_y = new_y
