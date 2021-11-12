import random
from dataclasses import dataclass
from typing import Any

from creature import Creature


@dataclass
class Prey(Creature):
    def __init__(self) -> None:
        super().__init__()

    def set_starting_position(self, creature: Any = None) -> bool:
        if creature is None:
            print("Illegal Prey Creation")
            return False
        self.position = random.randint(creature.position + 1, 100)
        return True
