from random import randint

class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


six_sides_die = Die()
ten_sides_die = Die(10)
twenty_sides_die = Die(20)

for count in range(10):
    six_sides_die.roll_die()


for count in range(10):
    ten_sides_die.roll_die()


for count in range(10):
    twenty_sides_die.roll_die()

