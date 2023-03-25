import random as r
import arcade as a

from auto_mobile import Automobile
from stop_light import StopLight

class TrafficSim(a.Window):

    BLACK = a.color.BLACK
    WHITE = a.color.WHITE
    RED = a.color.RED
    GREEN = a.color.GREEN

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        a.set_background_color(self.BLACK)

        # Create the cars
        self.cars = a.SpriteList()
        for i in range(10):
            # C:\Users\Lauren\anaconda3\envs\machine_learning\Lib\site-packages\arcade\resources\gui_basic_assets\items
            car = Automobile(":resources:gui_basic_assets/items/shield_gold.png".format(r.randint(1, 7)), 0.5)
            car.center_x = r.randint(0, self.width - car.width)
            car.center_y = self.height + car.length
            self.cars.append(car)

        # Create the intersection
        self.light = StopLight((self.width - StopLight.WIDTH) / 2, (self.height - StopLight.LENGTH) / 2)

    def on_draw(self):
        a.start_render()

        # Draw the cars
        self.cars.draw()

        # Draw the intersection
        a.draw_texture_rectangle(self.light.center_x, self.light.center_y, StopLight.WIDTH, StopLight.LENGTH, self.light.texture)

    def update(self, delta_time):
        # Move the cars
        for car in self.cars:
            if self.light.state == "green":
                car.update()

        # Check for collisions
        for car in self.cars:
            if car.collides_with_sprite(self.light):
                car.center_y = self.height + car.length

        # Update the intersection
        self.light.update(delta_time)