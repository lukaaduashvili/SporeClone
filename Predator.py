import random
from dataclasses import dataclass

from Creature import Creature


@dataclass
class Predator(Creature):
    def __init__(self) -> None:
        pass

    def set_starting_position(self) -> None:
        self.position = random.randint(0, 99)
