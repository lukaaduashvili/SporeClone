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
