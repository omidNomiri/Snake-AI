import arcade
from snake import Snake
from food import Meat
import pandas as pd
import numpy as np
from keras.models import load_model

# Movement directions for the snake
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class Game(arcade.Window):
    def __init__(self):
        # Initialize the game window
        super().__init__(width=512, height=512, title='Super Snake')
        arcade.set_background_color(arcade.color.KHAKI)

        # Create snake and food objects
        self.snake = Snake(self)
        self.food = Meat(self)
        self.score = 0

        # Load the trained model
        self.model = load_model('model/snake_direction_model.h5')

    def on_draw(self):
        # Start rendering
        arcade.start_render()

        # Draw the snake and food
        self.snake.draw()
        self.food.draw()

        # Display the game score
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.BLACK, 14)

        # Finish rendering
        arcade.finish_render()

    def on_update(self, delta_time):
        # Move the snake
        self.snake.move()

        # Calculate the positions and distances related to walls and food
        data = {
            'wall_up': self.height - self.snake.center_y,
            'wall_right': self.width - self.snake.center_x,
            'wall_down': self.snake.center_y,
            'wall_left': self.snake.center_x,
            'apple_up': int(self.snake.center_y < self.food.center_y),
            'apple_right': int(self.snake.center_x < self.food.center_x),
            'apple_down': int(self.snake.center_y > self.food.center_y),
            'apple_left': int(self.snake.center_x > self.food.center_x),
            'distance_x': self.snake.center_x - self.food.center_x,
            'distance_y': self.snake.center_y - self.food.center_y
        }

        # Create a DataFrame for prediction
        data_df = pd.DataFrame([data])

        # Make predictions using the model
        output = self.model.predict(data_df)
        prediction = np.argmax(output)

        # Update the snake's direction based on the prediction
        if prediction == UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif prediction == RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif prediction == DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif prediction == LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0

        # Update the snake and food states
        self.snake.on_update()
        self.food.on_update()

        # Check for collision between the snake and food
        if arcade.check_for_collision(self.snake, self.food):
            self.snake.eat_meat(self.food)
            self.score += 1
            self.food = Meat(self)  # Create a new food item

    def on_key_press(self, symbol: int, modifiers: int):
        # Handle key press events
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()  # Close the window
            arcade.exit()  # Exit the game

if __name__ == "__main__":
    # Run the game
    game = Game()
    arcade.run()
