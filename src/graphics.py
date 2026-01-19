# Game window and rendering
import tkinter as tk
from .config import *


class GameWindow:
    def __init__(self, game):
        """Initialize game window"""
        self.game = game

        # Create main window
        self.window = tk.Tk()
        self.window.title("Snake game")
        self.window.resizable(False, False)

        # Create canvas for drawing
        self.canvas = tk.Canvas(
            self.window,
            bg=BACKGROUND_COLOR,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            borderwidth=0,
            highlightthickness=0,
        )
        self.canvas.pack()
        self.window.update()

        # Center window on screen
        self._center_window()

        # Bind keyboardevents
        self.window.bind(
            "<KeyRelease>", self._on_key_press
        )

    def _center_window(self):
        """Center the window on screen"""
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()
        screen_width = (
            self.window.winfo_screenwidth()
        )
        screen_height = (
            self.window.winfo_screenheight()
        )

        window_x = int(
            (screen_width / 2) - window_width / 2
        )
        window_y = int(
            (screen_height / 2)
            - window_height / 2
        )

        self.window.geometry(
            f"{window_width}x{window_height}+{window_x}+{window_y}"
        )

    def _on_key_press(self, event):
        """Handle key press events"""
        self.game.change_direction(event.keysym)

    def _draw_game(self):
        """Draw current game state"""
        self.canvas.delete("all")

        # Draw food
        self.canvas.create_rectangle(
            self.game.food.x,
            self.game.food.y,
            self.game.food.x + TILE_SIZE,
            self.game.food.y + TILE_SIZE,
            fill=FOOD_COLOR,
        )

        # Draw snake head
        self.canvas.create_rectangle(
            self.game.snake.x,
            self.game.snake.y,
            self.game.snake.x + TILE_SIZE,
            self.game.snake.y + TILE_SIZE,
            fill=SNAKE_COLOR,
        )

        # Draw snake body
        for tile in self.game.snake_body:
            self.canvas.create_rectangle(
                tile.x,
                tile.y,
                tile.x + TILE_SIZE,
                tile.y + TILE_SIZE,
                fill=SNAKE_COLOR,
            )

        # Draw score
        self.canvas.create_text(
            40,
            20,
            font="Arial 15",
            text=f"Score: {self.game.score}",
            fill=TEXT_COLOR,
        )

    def _draw_game_over(self):
        """Draw game over screen"""
        self.canvas.delete("all")
        self.canvas.create_text(
            WINDOW_WIDTH / 2,
            WINDOW_HEIGHT / 2,
            font="Arial 30",
            text=f"Score: {self.game.score}",
            fill=TEXT_COLOR,
        )

    def _game_loop(self):
        """Main game loop"""
        if self.game.update():
            self._draw_game()
        else:
            self._draw_game_over()

        # Schedule next frame
        self.window.after(
            GAME_SPEED, self._game_loop
        )

    def run(self):
        """Start the game"""
        self._game_loop()
        self.window.mainloop()
