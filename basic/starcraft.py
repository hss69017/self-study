from random import *

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("Unit {0} is created.".format(name))

    def move(self, location):
        print("{0} moves to {1}. [speed {2}]".format(self.name, location, self.speed))

    def damaged(self, atk):
        print("{0} is damaged as {1} point(s).".format(self.name, atk))
        self.hp -= atk
        print("{0}'s hp is {1}.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} is destoryed.".format(self.name))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, atk):
        Unit.__init__(self, name, hp, speed)
        self.atk = atk

    def attack(self, location):
        print("{0} attacks enemies in {1}. [Attack {2}]".format(self.name, location, self.atk))

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "marine", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("Unit {0} uses stimpack. [HP 10 decreasing]".format(self.name))
        else:
            print("Unit {0} can't use stimpack because of low hp.".format(self.name))

class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "tank", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        if self.seize_mode == False:
            print("Unit {0} is changed to seize mode.".format(self.name))
            self.atk *= 2
            self.seize_mode = True
        else:
            print("Unit {0} is changed to unseize mode.".format(self.name))
            self.atk /= 2
            self.seize_mode = False

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
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "wraith", 80, 20, 5)
        self.cloaked = False
    
    def cloaking(self):
        if self.cloaked == True:
            print("{0} is uncloaked.".format(self.name))
            self.cloaked = False
        else:
            print("{0} is cloaked.".format(self.name))
            self.cloaked = True

def game_start():
    print("[notice] The new game is started.")

def game_over():
    print("Player: gg")
    print("[Player] exited from the game.")

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1 o'clock")

Tank.seize_developed = True
print("[notice] Tank seize mode technique is developed.")

for unit in attack_units:
    if isinstance(unit, Marine): #instance가 특정 class의 객체(instance)인지 확인
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.cloaking()

for unit in attack_units:
    unit.attack("1 o'clock")

for unit in attack_units:
    unit.damaged(randint(5, 20))

game_over()