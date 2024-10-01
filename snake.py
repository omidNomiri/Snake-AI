import arcade


class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.body = []
        self.width = 32
        self.height = 32

        self.center_x = game.width//2
        self.center_y = game.height//2
        self.change_x = 0
        self.change_y = 0
        
        self.color = arcade.color.BROWN
        self.colorbody = arcade.color.DEEP_COFFEE

        self.speed = 3
        self.score = 0

        self.w = game.width
        self.h = game.height

    def draw(self):
        arcade.draw_circle_filled(
            self.center_x, self.center_y, 15, self.color)

        for i, part in enumerate(self.body):
            if i % 2 == 0:
                self.colorbody = arcade.color.DEEP_COFFEE
            elif i % 2 == 1:
                self.colorbody = arcade.color.WOOD_BROWN

            arcade.draw_circle_filled(
                part['x'], part['y'], 15, self.colorbody)

    def move(self):
        self.body.append({'x': self.center_x, 'y': self.center_y})
        if len(self.body) > self.score:
            for _ in range(len(self.body)-self.score):
                self.body.pop(0)

        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed



    def eat_meatloaf(self, meatloaf):
        # Handle eating meatloaf
        self.score += 2
        del meatloaf

    def eat_meat(self, meat):
        # Handle eating meat
        self.score += 1
        del meat

    def eat_plant(self, plant):
        # Handle eating plant
        self.score -= 1
        del plant
        if not self.body:
            arcade.draw_text("GAME OVER!", 150, 300, arcade.color.RED_DEVIL, 35)
            self.score = 0


    def game_over(self):
        arcade.draw_text("GAME OVER!", 150, 300, arcade.color.RED_DEVIL, 35)
        self.score = 0
        self.body = []
