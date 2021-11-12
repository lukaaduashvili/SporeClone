from creature import Creature


class Attack:
    @staticmethod
    def hit_creature(hitter: Creature, hit: Creature) -> None:
        attack_power = hitter.power * (hitter.claws * 2) + hitter.teeth * 3
        hit.health -= attack_power
