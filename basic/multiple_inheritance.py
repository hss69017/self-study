#다중상속(multiple inheritance)

class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit):
    def __init__(self, name, hp, atk):
        Unit.__init__(self, name, hp)
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
        print("{0} flies to {1}. [speed: {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, atk, flying_speed):
        AttackUnit.__init__(self, name, hp, atk)
        Flyable.__init__(self, flying_speed)

valkyrie = FlyableAttackUnit("valkyrie", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3 o'clock")