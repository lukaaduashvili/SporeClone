from Predator import Predator
from Prey import Prey

prey = Prey()
pred = Predator()


def test_predator_and_prey_location() -> None:

    pred.set_starting_position()
    prey.set_starting_position(pred)

    assert pred.position < prey.position
