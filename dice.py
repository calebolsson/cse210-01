import random


class die:
    def __init__(self, default=6) -> None:
        self.sides = default

    def getSides(self):
        print(f"{self.sides}")

    def roll(self):
        return random.randrange(1, self.sides)


class score:
    def __init__(self) -> None:
        self.points = 0

    def getScore(self):
        # print(f"{self.points}")
        return self.points

    def addPoints(self, add):
        self.points += add


p1score = score()
points = 0
d6 = die()
playing = True
while (playing):
    command = input("Roll dice? (y/n) ")
    if command == '' or command[0] == 'y':
        rolls = [d6.roll(), d6.roll(), d6.roll(), d6.roll(), d6.roll()]
        print("You rolled:", rolls[:])
        points = 0
        for i in rolls:
            if i == 1:
                points += 100
            elif i == 5:
                points += 50
        p1score.addPoints(points)
        print("Score:", str(p1score.getScore()), "(+"+str(points)+")")
        if points == 0:
            print("Game Over!")
            playing = False
        print()
    else:
        playing = False
