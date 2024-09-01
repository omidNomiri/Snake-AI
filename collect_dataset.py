import arcade
import pandas as pd
from snake import Snake
from food import Meat


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height=600, title="AI Snake Game")
        arcade.set_background_color(arcade.color.KHAKI)

        self.meat = Meat(self)
        self.snake = Snake(self)
        self.snake.score = 0

        self.state_df = pd.DataFrame(columns=[
            'wall_up', 'wall_right', 'wall_down', 'wall_left',
            'meat_up', 'meat_right', 'meat_down', 'meat_left',
            'body_up', 'body_right', 'body_down', 'body_left'
        ])

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(f"Score: {self.snake.score}", 10, 10)
        self.snake.draw()
        self.meat.draw()
        arcade.finish_render()

    def log_state(self):
        if len(self.snake.body) == 0:
            return

        head_x, head_y = self.snake.body[0]['x'], self.snake.body[0]['y']

        wall_up = head_y
        wall_right = self.width - head_x
        wall_down = self.height - head_y
        wall_left = head_x

        meat_up = self.meat.center_y - head_y if self.meat.center_y > head_y else 0
        meat_right = self.meat.center_x - head_x if self.meat.center_x > head_x else 0
        meat_down = head_y - self.meat.center_y if self.meat.center_y < head_y else 0
        meat_left = head_x - self.meat.center_x if self.meat.center_x < head_x else 0

        body_up = min([segment['y'] - head_y for segment in self.snake.body[1:] if segment['y'] > head_y], default=0)
        body_right = min([segment['x'] - head_x for segment in self.snake.body[1:] if segment['x'] > head_x], default=0)
        body_down = min([head_y - segment['y'] for segment in self.snake.body[1:] if segment['y'] < head_y], default=0)
        body_left = min([head_x - segment['x'] for segment in self.snake.body[1:] if segment['x'] < head_x], default=0)

        state = pd.DataFrame([{
            'wall_up': wall_up, 'wall_right': wall_right, 'wall_down': wall_down, 'wall_left': wall_left,
            'meat_up': meat_up, 'meat_right': meat_right, 'meat_down': meat_down, 'meat_left': meat_left,
            'body_up': body_up, 'body_right': body_right, 'body_down': body_down, 'body_left': body_left
        }])

        self.state_df = pd.concat([self.state_df, state], ignore_index=True)

        if len(self.state_df) >= 10000:
            self.save_log_to_csv()

    def save_log_to_csv(self):
        self.state_df.to_csv('dataset/snake_state_dataset.csv', index=False)
        arcade.close_window()

    def on_update(self, delta_time: float):
        if arcade.check_for_collision(self.snake, self.meat):
            self.snake.eat_meat(self.meat)
            self.meat = Meat(self)

        self.snake.move_with_ai(self.meat.center_x, self.meat.center_y)
        self.snake.move()

        self.log_state()


if __name__ == "__main__":
    game = Game()
    arcade.run()
