class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[army unit moving]")
        print("{0} moves to {1}. [speed {2}]".format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, atk):
        Unit.__init__(self, name, hp, speed)
        self.atk = atk

    def attack(self, location):
        print("{0} attacks enemies in {1}. [Attack {2}]".format(self.name, location, self.atk))

    def damaged(self, atk):
        print("{0} is damaged as {1} point(s).".format(self.name, atk))
        self.hp -= atk
        print("{0}'s hp is {1}.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} is destoryed.".format(self.name))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} flies to {1}. [speed {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, atk, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, atk)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[air force unit moving]")
        self.fly(self.name, location) # method overriding

vulture = AttackUnit("vulture", 80, 10, 20)
battlecruiser = FlyableAttackUnit("battlecruiser", 500, 25, 3)

vulture.move("11 o'clock")
# battlecruiser.fly(battlecruiser.name, "9 o'clock")
battlecruiser.move("9 o'clock")