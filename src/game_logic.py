# Game logic- movement, collisions, state menagement

import random
from .tile import Tile
from .config import *
from .sound import Sound


class Game:
    def __init__(self):
        """Initialize game state"""
        self.sound = Sound()
        self.reset_game()

    def reset_game(self):
        """Reset game to initial state"""
        # Create snake head
        self.snake = Tile(
            INITIAL_SNAKE_X * TILE_SIZE,
            INITIAL_SNAKE_Y * TILE_SIZE,
        )

        # Create food
        self.food = Tile(
            INITIAL_FOOD_X * TILE_SIZE,
            INITIAL_FOOD_Y * TILE_SIZE,
        )

        # Initialize game variables
        self.snake_body = (
            []
        )  # multiple snake tiles
        self.velocityX = 0
        self.velocityY = 0
        self.game_over = False
        self.score = 0

    def change_direction(self, direction):
        """Change snake movement direction"""
        if self.game_over:
            return

        # Prevent 180 degree turns
        if (
            direction == "Up"
            and self.velocityY != 1
        ):
            self.velocityX = 0
            self.velocityY = -1
        elif (
            direction == "Right"
            and self.velocityX != -1
        ):
            self.velocityX = 1
            self.velocityY = 0
        elif (
            direction == "Down"
            and self.velocityY != -1
        ):
            self.velocityX = 0
            self.velocityY = 1
        elif (
            direction == "Left"
            and self.velocityX != 1
        ):
            self.velocityX = -1
            self.velocityY = 0

    def update(self):
        """Update game state - returns True if game continues"""
        if self.game_over:
            return False

        # Check wall collision
        if (
            self.snake.x < 0
            or self.snake.x >= WINDOW_WIDTH
            or self.snake.y < 0
            or self.snake.y >= WINDOW_HEIGHT
        ):
            self.game_over = True
            self.sound.sound_game_over()
            return False

        # Check self collision
        for tile in self.snake_body:
            if (
                self.snake.x == tile.x
                and self.snake.y == tile.y
            ):
                self.game_over = True
                self.sound.sound_game_over()
                return False

        # Check food collision
        if (
            self.snake.x == self.food.x
            and self.snake.y == self.food.y
        ):
            self.snake_body.append(
                Tile(self.food.x, self.food.y)
            )
            self.food.x = (
                random.randint(0, COLS - 1)
                * TILE_SIZE
            )
            self.food.y = (
                random.randint(0, ROWS - 1)
                * TILE_SIZE
            )
            self.score += 1
            self.sound.sound_eat()

        # Update snake body position
        for i in range(
            len(self.snake_body) - 1, -1, -1
        ):
            tile = self.snake_body[i]
            if i == 0:
                # First body segment follows head
                tile.x = self.snake.x
                tile.y = self.snake.y
            else:
                # Other segments follow previous segment
                prev_tile = self.snake_body[i - 1]
                tile.x = prev_tile.x
                tile.y = prev_tile.y

        # Move snake head
        self.snake.x += self.velocityX * TILE_SIZE
        self.snake.y += self.velocityY * TILE_SIZE

        return True
