from src.graphics import GameWindow
from src.game_logic import Game


def main():
    """Main function to run the game"""
    # Create game instance
    game = Game()

    # Create game window with the game instance
    window = GameWindow(game)

    # Start the game
    window.run()


if __name__ == "__main__":
    main()
