import random

from creature import Creature


class EvolveCreature:
    @staticmethod
    def __evolve_legs(creature: Creature) -> None:
        creature.legs = random.randint(0, 2)

    @staticmethod
    def __evolve_wings(creature: Creature) -> None:
        creature.wings = random.randint(0, 2)

    @staticmethod
    def __evolve_claws(creature: Creature) -> None:
        creature.claws = random.randint(2, 4)

    @staticmethod
    def __evolve_teeth(creature: Creature) -> None:
        creature.teeth = random.randint(1, 3)

    @staticmethod
    def evolve_creature(creature: Creature) -> None:
        EvolveCreature.__evolve_wings(creature)
        EvolveCreature.__evolve_teeth(creature)
        EvolveCreature.__evolve_claws(creature)
        EvolveCreature.__evolve_legs(creature)
