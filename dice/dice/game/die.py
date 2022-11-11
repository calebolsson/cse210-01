import random


# TODO: Implement the Die class as follows...

# 1) Add the class declaration. Use the following class comment.
class Die:
    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.

    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
    """

# 2) Create the class constructor. Use the following method comment.
    def __init__(self, default=6):
        self.value = 0
        self.points = 0
        self.sides = default
        self.scoremap = [100, 0, 0, 0, 50, 0]
        """Constructs a new instance of Die with a value and points attribute.

        Args:
            self (Die): An instance of Die.
        """

# 3) Create the roll(self) method. Use the following method comment.
    def roll(self):
        self.value = random.randrange(1, self.sides)
        self.points = self.scoremap[self.value - 1]
        """Generates a new random value and calculates the points.
        
        Args:
            self (Die): An instance of Die.
        """
