import random


class Die:
    """
    Represents a dice with a specified number of sides.

    Attributes:
        sides (int): Number of sides on the dice.
    """

    def __init__(self, sides):
        """
        Initializes a new instance of the Die class.

        Args:
            sides (int): Number of sides for the dice. Should be between 2 and 1000.

        Raises:
            ValueError: If the number of sides is not between 2 and 1000.
        """
        if 2 <= sides <= 1000:
            self.sides = sides
        else:
            raise ValueError("Number of sides should be between 2 and 1000")

    def roll(self):
        """
        Rolls the dice and returns a random number between 1 and the number of sides.

        Returns:
            int: A random number representing the result of the dice roll.
        """
        return random.randint(1, self.sides)
