#super를 쓸 때는 ()써야 하고, self를 안 쓴다.

class Unit:
    def __init__(self):
        print("Unit __init__")

class Flyable:
    def __init__(self):
        print("Flyable __init__")

# class FlyableUnit(Unit, Flyable): #Unit __init__ is called only.
#     def __init__(self):
#         super().__init__()
# dropship = FlyableUnit()

# class FlyableUnit(Flyable, Unit): #Flyable __init__ is called only.
#     def __init__(self):
#         super().__init__()
# dropship = FlyableUnit()

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)
dropship = FlyableUnit()