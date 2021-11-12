from creature import Creature
from move import Move


class MoveCreatures:
    @staticmethod
    def move_with_logic(creature: Creature) -> bool:
        if creature.stamina >= creature.move_type.req_stamina:
            creature.position += creature.move_type.step_size
            creature.stamina -= creature.move_type.curr_stamina
            return True
        return False

    @staticmethod
    def set_move(creature: Creature, move_type: Move) -> bool:
        if (
            creature.stamina >= move_type.req_stamina
            and creature.legs >= move_type.req_legs
            and creature.wings >= move_type.req_wings
        ):
            creature.move_type = move_type
            return True
        return False
