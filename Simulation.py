from Attack import Attack
from Creature import Creature
from Move import Move
from Predator import Predator
from Prey import Prey


class Simulation:
    predator: Predator
    prey: Prey
    stalemate: int = 0
    predator_wins: int = 0
    prey_wins: int = 0

    def place_creatures(self) -> None:
        self.predator = Predator()
        self.prey = Prey()

        self.predator.evolve_creature()
        self.prey.evolve_creature()
        self.predator.set_starting_position()
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
            Move.move_from_position(self.prey)
            Move.move_from_position(self.predator)
            if self.predator.position >= self.prey.position:
                self.simulate_fighting()
                break

            if self.predator.stamina == 0 and self.prey.stamina == 0:
                print("Stalemate has occurred")
                self.stalemate += 1
                break
            elif self.predator.stamina == 0:
                print("Pray ran into infinity")
                self.prey_wins += 1
                break

    def simulate_fighting(self) -> None:
        while True:
            Attack.hit_creature(self.predator, self.prey)
            if self.prey.health <= 0:
                print("Some R rated things have happened")
                self.predator_wins += 1
                break
            Attack.hit_creature(self.prey, self.predator)
            if self.predator.health <= 0:
                print("Prey ran into infinity")
                self.prey_wins += 1
                break

    def begin_simulation(self) -> None:
        num_sim = 1000
        for i in range(num_sim):
            self.place_creatures()
            self.simulate_running()
        print(
            "Predator win change: "
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
