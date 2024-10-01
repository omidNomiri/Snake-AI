import arcade
from snake import Snake
from food import Meat
import pandas as pd

# Directions for snake movement
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=512, height=512, title='Super Snake')
        arcade.set_background_color(arcade.color.KHAKI)

        self.snake = Snake(self)  # Create snake object
        self.meat = Meat(self)    # Create food object
        self.score = 0            # Initialize score

        self.data = []            # List to store game state data

    def on_draw(self):
        """Render game elements"""
        arcade.start_render()
        arcade.draw_text(f"Score: {self.score}", 10, 10)  # Display score
        self.snake.draw()  # Render the snake
        self.meat.draw()   # Render the food
        arcade.finish_render()

    def on_update(self, delta_time: float):
        """Update game state"""
        # Save game state to CSV after collecting 10,000 records
        if len(self.data) >= 10000:
            df = pd.DataFrame(self.data)
            df.to_csv('dataset/snake_state_dataset.csv', index=False)
            arcade.close_window()
            arcade.exit()

        # Update snake position
        self.snake.move()

        # Calculate distance to food
        distance_x = self.snake.center_x - self.meat.center_x
        distance_y = self.snake.center_y - self.meat.center_y

        # Create a dictionary to store game state
        data = {
            'wall_up': self.height - self.snake.center_y,
            'wall_down': self.snake.center_y,
            'wall_left': self.snake.center_x,
            'wall_right': self.width - self.snake.center_x,
            'meat_up': int(self.snake.center_y < self.meat.center_y and abs(distance_x) < self.snake.width),
            'meat_right': int(self.snake.center_x < self.meat.center_x and abs(distance_y) < self.snake.height),
            'meat_down': int(self.snake.center_y > self.meat.center_y and abs(distance_x) < self.snake.width),
            'meat_left': int(self.snake.center_x > self.meat.center_x and abs(distance_y) < self.snake.height),
            'distance_x': distance_x,
            'distance_y': distance_y,
            'direction': None  # Placeholder for direction
        }

        # Simplify snake movement logic
        if abs(distance_x) > abs(distance_y):
            if distance_x > 0:
                self.snake.change_x = -1
                self.snake.change_y = 0
                data['direction'] = LEFT
                print("LEFT")
            else:
                self.snake.change_x = 1
                self.snake.change_y = 0
                data['direction'] = RIGHT
                print("RIGHT")
        else:
            if distance_y > 0:
                self.snake.change_x = 0
                self.snake.change_y = -1
                data['direction'] = DOWN
                print("DOWN")
            else:
                self.snake.change_x = 0
                self.snake.change_y = 1
                data['direction'] = UP
                print("UP")

        # Add data to the list if all values are not None
        if all(v is not None for v in data.values()):
            self.data.append(data)

        # Update snake and food status
        self.snake.on_update(delta_time)
        self.meat.on_update()

        # Check for collision between snake and food
        if arcade.check_for_collision(self.snake, self.meat):
            self.snake.eat_meat(self.meat)
            self.score += 1
            self.meat = Meat(self)  # Generate new food
            print("Meat eaten")

if __name__ == '__main__':
    game = Game()
    arcade.run()
