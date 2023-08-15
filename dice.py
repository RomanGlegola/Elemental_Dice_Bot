# Elemental_Dice_Bot is Copyright (C) 2023 <Roman Glegola>
#
# Elemental_Dice_Bot is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation version 3 of the License.
#
# Elemental_Dice_Bot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Elemental_Dice_Bot. If not, see <http://www.gnu.org/licenses/>.

import random


class Die:
    """
    Represents a dice with a specified number of sides.

    Attributes:
        sides (int): Number of sides on the dice.
    """

    def __init__(self, sides: int):
        """
        Initializes a new instance of the Die class.

        Args:
            sides (int): Number of sides for the dice. Should be between 2 and 1000.

        Raises:
            ValueError: If the number of sides is not between 2 and 1000.
        """
        if 2 <= sides <= 1000:
            self.sides: int = sides
        else:
            raise ValueError("Number of sides should be between 2 and 1000")

    def roll(self) -> int:
        """
        Rolls the dice and returns a random number between 1 and the number of sides.

        Returns:
            int: A random number representing the result of the dice roll.
        """
        return random.randint(1, self.sides)
