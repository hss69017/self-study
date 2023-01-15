#상속(inheritance)

class Unit: #부모 class
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit): #자식 class
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

firebat1 = AttackUnit("firebat", 50, 16)
firebat1.attack("5 o'clock")
firebat1.damaged(25)
firebat1.damaged(25)