import random
from .prototypes import circulo_food

class circle_creator():
    def __init__(self):
        self.__circulo__ = circulo_food()

    def get_circle(self):
        self.__circulo__.set_position(random.randrange(1000), random.randrange(1000))
        self.__circulo__.set_color(random.randrange(255), random.randrange(255), random.randrange(255))
        return self.__circulo__.clone()

    