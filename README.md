# Pong Game

This repository contains a simple implementation of the classic arcade game, Pong, using the Python Turtle graphics module. The game features a two-player mode, with each player controlling a paddle using keyboard inputs. The objective is to score points by getting the ball past the opponent's paddle.

## Features
- Two-player gameplay
- Real-time score tracking with a scoreboard
- Ball movement with collision detection and bouncing
- Responsive paddle controls for each player
- Classic Pong gameplay experience

## How to Play
Player 1 (Left Paddle) Controls:
- `W` key to move up
- `S` key to move down

Player 2 (Right Paddle) Controls:
- `Up Arrow` key to move up
- `Down Arrow` key to move down

## Modules

The code is organized into several modules:

1. `paddles.py`: Contains the `Paddle` class, which defines the paddle objects and their movement methods.
2. `ball.py`: Contains the `Ball` class, which defines the ball object, its movement, and bouncing behavior.
3. `scoreboard.py`: Contains the `Scoreboard` class, which manages the score display and updates.

## Dependencies
- Python 3.x
- Turtle module

## Running the Game
To run the game, simply execute the main Python script:

```
python main.py
```

Enjoy the classic Pong experience and challenge your friends to a match!