import random
from dataclasses import dataclass


@dataclass
class Creature:
    position: int
    power: int = 1
    health: int = 100
    stamina: int = 100
    wings: int = 0
    legs: int = 0
    claws: int = 0
    teeth: int = 0
    crawling: bool = True

    def __init__(self) -> None:
        pass

    def evolve_legs(self) -> None:
        self.legs = random.randint(0, 2)

    def evolve_wings(self) -> None:
        self.wings = random.randint(0, 2)

    def evolve_claws(self) -> None:
        self.claws = random.randint(2, 4)

    def evolve_teeth(self) -> None:
        self.teeth = random.randint(1, 3)

    def evolve_creature(self) -> None:
        self.evolve_wings()
        self.evolve_teeth()
        self.evolve_claws()
        self.evolve_legs()
