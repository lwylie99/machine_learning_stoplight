import arcade

class Automobile(arcade.Sprite):
    speed = 5
    width = 30
    length = 60
    
    # def __init__(self, speed, width, length):
    #     super().__init__()
    #     self.speed = speed
    #     self.width = width
    #     self.length = length


    def update(self):
        self.center_y -= self.speed