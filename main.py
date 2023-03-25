import arcade
import random

from traffic_sim import Game


def main():
    # WINDOW_WIDTH = 800
    # WINDOW_HEIGHT = 600

    window = Game(800, 600, "Traffic Simulator")
    arcade.run()

if __name__ == "__main__":
    main()
