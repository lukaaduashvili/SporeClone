from dataclasses import dataclass

from Creature import Creature


@dataclass
class Move:
    @staticmethod
    def move_from_position(creature: Creature) -> None:
        if creature.wings == 2 and creature.stamina > 80:
            Move.move_with_logic(creature, 8, 4)
        elif creature.legs == 2 and creature.stamina > 60:
            Move.move_with_logic(creature, 6, 4)
        elif creature.legs == 2 and creature.stamina > 40:
            Move.move_with_logic(creature, 4, 2)
        elif creature.legs > 0 and creature.stamina > 20:
            Move.move_with_logic(creature, 3, 2)
        elif creature.stamina > 0:
            Move.move_with_logic(creature, 1, 1)

    @staticmethod
    def move_with_logic(creature: Creature, speed: int, stamina: int) -> None:
        if creature.stamina >= stamina:
            creature.position += speed
            creature.stamina -= stamina
