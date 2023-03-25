import arcade as a

class StopLight(a.Sprite):
    WIDTH = 200
    LENGTH = 200

    GREEN_TIME = 5000
    YELLOW_TIME = 1000
    RED_TIME = 5000

    BLACK = a.color.BLACK_LEATHER_JACKET
    WHITE = a.color.NAVAJO_WHITE
    RED = a.color.RUSTY_RED
    GREEN = a.color.TEA_GREEN
    YELLOW = a.color.YELLOW_ROSE

    def __init__(self, x, y):
        super().__init__()
        # self.texture = a.make_soft_square_texture(self.WIDTH, self.LENGTH, self.RED)
        self.texture = a.make_soft_square_texture(self.LENGTH, self.WHITE)
        self.position = (x, y)
        self.state = "red"
        self.timer = self.RED_TIME

    def update(self, delta_time):
        self.timer -= delta_time

        if self.timer > 0:
            return
        
        if self.state == "green":
            self.turnYellow()
        elif self.state == "yellow":
            self.turnRed()
        elif self.state == "red":
            self.turnGreen()

    def turnGreen(self):
        self.texture = a.make_soft_square_texture(self.LENGTH, self.GREEN)
        self.state = "green"
        self.timer = self.GREEN_TIME

    def turnYellow(self):
        self.texture = a.make_soft_square_texture(self.LENGTH, self.YELLOW)
        self.state = "yellow"
        self.timer = self.YELLOW_TIME

    def turnRed(self):
        self.texture = a.make_soft_square_texture(self.LENGTH, self.RED)
        self.state = "red"
        self.timer = self.RED_TIME