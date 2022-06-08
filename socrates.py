class Animal:
    color = None
    leg_number = None
    # can_fly = False

    def __init__(self, color, leg_number):
        self.color = color
        self.leg_number = leg_number
        # self.can_fly = can_fly

    def move(self):
        return "I'm moving with " + str(self.leg_number) + " legs!"
        # if self.can_fly:
        #     return "I'm flying!"
        # else:
        #     return "I'm moving with " + str(self.leg_number) + " legs!"

class Cat(Animal):
    pass

class Bug(Animal):
    pass

class Bird(Animal):
    can_fly = True

    def __init__(self, color, leg_number, can_fly):
        self.color = color
        self.leg_number = leg_number
        self.can_fly = can_fly

    def move(self):
        if self.can_fly:
            return "I'm flying"
        else:
            return "I'm moving with " + str(self.leg_number) + " legs!"

if __name__ == "__main__":
    cat = Cat("Orange", 4)
    bug = Bug("Black", 8)
    bird = Bird("Red", 2, True)
    print(cat.move())
    print(bug.move())
    print(bird.move())

