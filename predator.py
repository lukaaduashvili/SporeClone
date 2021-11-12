import random
from dataclasses import dataclass
from typing import Any

from creature import Creature


@dataclass
class Predator(Creature):
    def __init__(self) -> None:
        super().__init__()

    def set_starting_position(self, creature: Any = None) -> bool:
        if creature is None:
            self.position = random.randint(0, 99)
            return True
        print("Illegal Predator creation")
        return False
