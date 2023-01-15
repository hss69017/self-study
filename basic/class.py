# name = "marine"
# hp = 40
# atk = 5
# print("Unit {0} is created.".format(name))
# print("HP {0}, Attack {1}\n".format(hp, atk))

# tank_name = "tank"
# tank_hp = 150
# tank_atk = 35
# print("Unit {0} is created.".format(tank_name))
# print("HP {0}, Attack {1}\n".format(tank_hp, tank_atk))

# tank2_name = "tank"
# tank2_hp = 150
# tank2_atk = 35
# print("Unit {0} is created.".format(tank2_name))
# print("HP {0}, Attack {1}\n".format(tank2_hp, tank2_atk))

# def attack(name, location, atk):
#     print("{0} attacks enemies in {1}. [Attack: {2}]".format(name, location, atk))
# attack(name, "1 o'clock", atk)
# attack(tank_name, "1 o'clock", tank_atk)
# attack(tank2_name, "1 o'clock", tank2_atk)

class Unit:
    def __init__(self, name, hp, atk): #__init__은 생성자
        self.name = name #self.name 등은 멤버변수
        self.hp = hp
        self.atk = atk
        print("Unit {0} is created.".format(self.name))
        print("HP {0}, Attack {1}".format(self.hp, self.atk))

# marine1 = Unit("marine", 40, 5) #class로부터 만들어지는 marine1 등은 객체
# marine2 = Unit("marine", 40, 5) #marine1 등은 Unit class의 instance라고 표현
# tank = Unit("tank", 150, 35)

# wraith1 = Unit("wraith", 80, 5)
# print("unit name: {0}, attack: {1}".format(wraith1.name, wraith1.atk))

# wraith2 = Unit("lost wraith", 80, 5)
# wraith2.clocking = True #class 외부에서도 변수 확장 가능, 단 내가 선언한 객체에만 적용
# if wraith2.clocking == True:
#     print("{0} is cloaked.".format(wraith2.name))

class AttackUnit:
    def __init__(self, name, hp, atk): #__init__은 생성자
        self.name = name #self.name 등은 class의 멤버변수
        self.hp = hp
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