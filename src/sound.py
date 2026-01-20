# Sound effects for the game

import os
import threading
from pathlib import Path


class Sound:
    _SOUND_PATHS = {
        "eat": "assets/sounds/eat.wav",
        "game_over": "assets/sounds/game_over.mp3",
    }

    def __init__(self):
        self.enabled = True
        self.root = Path(__file__).parent.parent

    def _play(self, name):
        if not self.enabled:
            return

        path = self.root / self._SOUND_PATHS[name]

        if not path.exists():
            return

        def play():
            os.system(f"afplay '{path}' &")

        threading.Thread(
            target=play, daemon=True
        ).start()

    def sound_eat(self):
        self._play("eat")

    def sound_game_over(self):
        self._play("game_over")
