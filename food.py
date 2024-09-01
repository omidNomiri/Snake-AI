from random import randint
import arcade

class Meatloaf(arcade.Sprite):
    def __init__(self,game):
        super().__init__("sources/meatloaf.png")
        self.width = 36
        self.height = 36
        self.center_x = randint(10,game.width - 10)
        self.center_y = randint(10,game.height - 10)
        self.change_x = 0
        self.change_y = 0

class Meat(arcade.Sprite):
    def __init__(self,game):
        super().__init__("sources/meat.png")
        self.width = 36
        self.height = 36
        self.center_x = randint(10,game.width - 10)
        self.center_y = randint(10,game.height - 10)
        self.change_x = 0
        self.change_y = 0

class Plant(arcade.Sprite):
    def __init__(self, game):
        super().__init__("sources/plant.png")
        self.width = 36
        self.height = 36
        self.center_x = randint(10,game.width - 10)
        self.center_y = randint(10,game.height - 10)
        self.change_x = 0
        self.change_y = 0
