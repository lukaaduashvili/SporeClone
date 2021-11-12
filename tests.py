from attack import Attack
from evolve_creature import EvolveCreature
from move import Crawl, Fly, Run, Walk
from move_creatures import MoveCreatures
from predator import Predator
from prey import Prey
from simulation import Simulation

prey = Prey()
pred = Predator()


def test_predator_and_prey_location() -> None:

    pred.set_starting_position()
    prey.set_starting_position(pred)

    assert pred.position < prey.position

    assert pred.set_starting_position(prey) is False
    assert prey.set_starting_position() is False


def test_creature_generation() -> None:
    EvolveCreature.evolve_creature(pred)
    assert 2 >= pred.legs >= 0
    assert 2 >= pred.wings >= 0
    assert 4 >= pred.claws >= 2
    assert 3 >= pred.teeth >= 1


def test_attack_creatures() -> None:
    prey.health = 5
    pred.teeth = 4
    pred.claws = 3
    assert not prey.is_dead()
    Attack.hit_creature(pred, prey)
    assert prey.is_dead()


def test_move_creatures() -> None:
    pred.legs = 2
    pred.stamina = 100
    pred.position = 0
    assert MoveCreatures.set_move(pred, Run())

    MoveCreatures.move_with_logic(pred)
    assert pred.position == 6

    pred.wings = 1
    assert not MoveCreatures.set_move(pred, Fly())

    assert MoveCreatures.set_move(pred, Walk())
    MoveCreatures.move_with_logic(pred)
    assert pred.position == 10

    pred.stamina = 1
    assert not pred.is_tired()
    assert not MoveCreatures.move_with_logic(pred)

    MoveCreatures.set_move(pred, Crawl())
    assert MoveCreatures.move_with_logic(pred)
    assert pred.is_tired()


def test_simulation() -> None:
    pred.position = 1
    pred.stamina = 100
    pred.teeth = 3
    pred.claws = 3
    pred.wings = 2
    EvolveCreature.evolve_creature(prey)
    prey.position = 2
    prey.wings = 0
    simulation = Simulation(prey, pred)
    simulation.begin_simulation(1)
    assert simulation.predator_wins == 1

    pred.position = 1
    pred.stamina = 100
    pred.teeth = 3
    pred.claws = 3
    pred.wings = 0
    pred.legs = 1
    EvolveCreature.evolve_creature(prey)
    prey.position = 90
    prey.wings = 2
    simulation = Simulation(prey, pred)
    simulation.begin_simulation(1)
    assert simulation.prey_wins == 1

    pred.position = 1
    pred.stamina = 100
    pred.teeth = 3
    pred.claws = 3
    pred.wings = 0
    pred.legs = 1
    EvolveCreature.evolve_creature(prey)
    prey.stamina = 100
    prey.position = 2
    prey.wings = 1
    prey.legs = 1
    simulation = Simulation(prey, pred)
    simulation.begin_simulation(1)
    assert simulation.stalemate == 1

    simulation = Simulation()
    simulation.begin_simulation()
    assert simulation.prey_wins + simulation.stalemate + simulation.predator_wins == 100

    num_tries = 55
    simulation = Simulation()
    simulation.begin_simulation(num_tries)
    assert simulation.prey_wins + simulation.stalemate + simulation.predator_wins == 55
