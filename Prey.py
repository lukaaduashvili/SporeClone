import random
from dataclasses import dataclass

from Creature import Creature


@dataclass
class Prey(Creature):
    def __init__(self) -> None:
        pass

    def set_starting_position(self, creature: Creature) -> None:
        self.position = random.randint(creature.position + 1, 100)
