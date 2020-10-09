import random
from copy import deepcopy

class circulo_food():
    def __init__(self):
        self.position = [random.randrange(800), random.randrange(600)]
        self.color = (random.randrange(255), random.randrange(255), random.randrange(255))
        self.radio = 2

    def set_position(self, x, y):
        self.position = [x,y]
    
    def get_position(self):
        return self.position

    def get_color(self):
        return self.color

    def set_color(self, r, g, b):
        self.color = [r, g, b]

    def get_radio(self):
        return self.radio
    
    def clone(self):
        return deepcopy(self)

    