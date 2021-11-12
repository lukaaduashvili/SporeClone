from dataclasses import dataclass


@dataclass
class Move:
    step_size: int = 0
    curr_stamina: int = 0
    req_stamina: int = 0
    req_wings: int = 0
    req_legs: int = 0


@dataclass
class Crawl(Move):
    step_size: int = 1
    curr_stamina: int = 1
    req_stamina: int = 0
    req_wings: int = 0
    req_legs: int = 0


@dataclass
class Hop(Move):
    step_size: int = 3
    curr_stamina: int = 2
    req_stamina: int = 20
    req_wings: int = 0
    req_legs: int = 1


@dataclass
class Walk(Move):
    step_size: int = 4
    curr_stamina: int = 2
    req_stamina: int = 40
    req_wings: int = 0
    req_legs: int = 2


@dataclass
class Run(Move):
    step_size: int = 6
    curr_stamina: int = 4
    req_stamina: int = 60
    req_wings: int = 0
    req_legs: int = 2


@dataclass
class Fly(Move):
    step_size: int = 8
    curr_stamina: int = 4
    req_stamina: int = 80
    req_wings: int = 2
    req_legs: int = 0
