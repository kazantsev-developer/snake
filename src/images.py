from PIL import Image, ImageTk
from pathlib import Path
import random
from .config import *


class FruitImages:
    def __init__(self):
        self.fruit_cache = {}

    def load(self, window):
        root = Path(__file__).parent.parent
        fruits_dir = root / FRUITS_DIR

        for fruit_name in FRUITS_IMAGES:
            fruit_path = fruits_dir / fruit_name

            if not fruit_path.exists():
                print(f"Файл не найден: {fruit_path}")
                continue

            try:
                img = Image.open(fruit_path)
                if img.size != (TILE_SIZE, TILE_SIZE):
                    img = img.resize((TILE_SIZE, TILE_SIZE))

                photo = ImageTk.PhotoImage(
                    img, master=window
                )
                self.fruit_cache[fruit_name] = photo

            except Exception as e:
                print(f"Ошибка: {fruit_name}: {e}")

    def get_random(self):
        if not self.fruit_cache:
            return None

        fruit_name = random.choice(
            list(self.fruit_cache.keys())
        )
        return self.fruit_cache[fruit_name]

    def get_by_name(self, fruit_name):
        return self.fruit_cache.get(fruit_name)
