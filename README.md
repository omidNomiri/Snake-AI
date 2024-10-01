# Super Snake Game

Welcome to the **Super Snake** game! This project is a fun and interactive implementation of the classic Snake game using Python's Arcade library, enhanced with machine learning to predict the snake's movement direction based on the current game state.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Gameplay](#gameplay)
- [License](#license)

## Features

- Control the snake to eat food and grow.
- Machine learning model predicts the snake's movement direction based on the state of the game.
- Real-time collision detection with walls and food.
- Score tracking.

## Technologies Used

- Python 3.11.7
- Arcade (for game development)
- Keras (for machine learning model)
- Pandas (for data manipulation)
- NumPy (for numerical operations)

## Installation

To get started with the Super Snake game, follow these steps:

1.Clone this repository:

```bash
git clone https://github.com/yourusername/super-snake.git
cd super-snake
```

2.Install the required packages:

```bash
pip install arcade keras pandas numpy
```

3.Download or create the model:

- Ensure you have a trained model saved as `snake_direction_model.h5` in the `model` directory.
- You can train your model using the provided dataset (`snake_state_dataset.csv`).

## Usage

To run the ai game, execute the following command:

```bash
python collect_dataset.py
```

after the program closed run this command:

```bash
python train.py
```

after you seen the plot run this command:

```bash
python main_ai.py
```

or just run one of this program:

```bash
python main_keyboard.py
```

```bash
python main_auto.py
```

The game window will open, and you can start playing or just chill and watch!

## Gameplay

- Use the arrow keys to control the direction of the snake.
- The objective is to eat the food (represented as meat) to score points and grow the snake.
- The game ends if the snake collides with the walls or itself.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
