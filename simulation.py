from typing import Optional

from attack import Attack
from creature import Creature
from evolve_creature import EvolveCreature
from move import Crawl, Fly, Hop, Run, Walk
from move_creatures import MoveCreatures
from predator import Predator
from prey import Prey


def simulate_moves(creature: Creature) -> None:
    if MoveCreatures.set_move(creature, Fly()):
        return
    elif MoveCreatures.set_move(creature, Run()):
        return
    elif MoveCreatures.set_move(creature, Walk()):
        return
    elif MoveCreatures.set_move(creature, Hop()):
        return
    else:
        MoveCreatures.set_move(creature, Crawl())


class Simulation:
    predator: Predator
    prey: Prey
    stalemate: int = 0
    predator_wins: int = 0
    prey_wins: int = 0

    def __init__(
        self, prey: Optional[Prey] = None, predator: Optional[Predator] = None
    ):
        if predator is None:
            self.predator = Predator()
            EvolveCreature.evolve_creature(self.predator)
            self.predator.set_starting_position()
        else:
            self.predator = predator

        if prey is None:
            self.prey = Prey()
            EvolveCreature.evolve_creature(self.prey)
            self.prey.set_starting_position(self.predator)
        else:
            self.prey = prey

        Simulation.print_attributes(self.prey)
        Simulation.print_attributes(self.predator)

    def generate_players(self) -> None:
        self.predator = Predator()
        EvolveCreature.evolve_creature(self.predator)
        self.predator.set_starting_position()
        self.prey = Prey()
        EvolveCreature.evolve_creature(self.prey)
        self.prey.set_starting_position(self.predator)
        Simulation.print_attributes(self.prey)
        Simulation.print_attributes(self.predator)

    @staticmethod
    def print_attributes(creature: Creature) -> None:
        name: str

        if type(creature) == Predator:
            name = "predator"
        else:
            name = "prey"

        print(
            "Generated "
            + name
            + " at position: "
            + str(creature.position)
            + "\n"
            + "Legs: "
            + str(creature.legs)
            + "\n"
            + "Wings: "
            + str(creature.wings)
            + "\n"
            + "Claws: "
            + str(creature.claws)
            + "\n"
            + "Teeth: "
            + str(creature.teeth)
            + "\n"
        )

    def simulate_running(self) -> None:
        while True:
            simulate_moves(self.prey)
            simulate_moves(self.predator)
            MoveCreatures.move_with_logic(self.prey)
            MoveCreatures.move_with_logic(self.predator)
            if self.predator.position >= self.prey.position:
                self.simulate_fighting()
                break

            if self.predator.is_tired() and self.prey.is_tired():
                print("Stalemate has occurred")
                self.stalemate += 1
                break
            elif self.predator.is_tired():
                print("Pray ran into infinity")
                self.prey_wins += 1
                break

    def simulate_fighting(self) -> None:
        while True:
            Attack.hit_creature(self.predator, self.prey)
            if self.prey.is_dead():
                print("Some R rated things have happened")
                self.predator_wins += 1
                break
            Attack.hit_creature(self.prey, self.predator)
            if self.predator.is_dead():
                print("Prey ran into infinity")
                self.prey_wins += 1
                break

    def begin_simulation(self, num_sim: int = 100) -> None:
        for i in range(num_sim):
            if i > 0:
                self.generate_players()
            self.simulate_running()
        print(
            "Predator win chance: "
            + str(self.predator_wins / num_sim * 100)
            + "%"
            + "\n"
            + "Prey win chance: "
            + str(self.prey_wins / num_sim * 100)
            + "%"
            + "\n"
            + "Stalemate chance: "
            + str(self.stalemate / num_sim * 100)
            + "%"
            + "\n"
        )
