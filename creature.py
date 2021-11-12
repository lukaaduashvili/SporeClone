import random
from dataclasses import dataclass
from typing import Any

from move import Crawl, Move


@dataclass
class Creature:
    position: int = 0
    power: int = 1
    health: int = 100
    stamina: int = 100
    wings: int = 0
    legs: int = 0
    claws: int = 0
    teeth: int = 0
    move_type: Move = Crawl()

    def __init__(self) -> None:
        pass

    def set_starting_position(self, creature: Any = None) -> bool:
        pass

    def is_tired(self) -> bool:
        if self.stamina == 0:
            return True
        return False

    def is_dead(self) -> bool:
        if self.health <= 0:
            return True
        return False
