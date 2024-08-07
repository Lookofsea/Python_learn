import random

class Dice:
    def rool(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return (first,second)


dice = Dice()
print(dice.rool())