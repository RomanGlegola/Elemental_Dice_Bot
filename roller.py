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

from typing import Optional

from dice import Die


class Roller:
    """Handles various types of dice rolls and related operations.

    Attributes:
        num_dice (int): Number of dice to be rolled.
        die (Die): Instance of Die class representing
            a dice with specified number of sides.
    """

    def __init__(self, num_dice: int, sides: int):
        """
        Initializes a new instance of the Roller class.

        Args:
            num_dice (int): Number of dice to be rolled.
            sides (int): Number of sides on each dice.
        """
        self.num_dice: int = num_dice
        self.die: Die = Die(sides)

    def normal_roll(
        self, modifier: int = 0
    ) -> tuple[list[int, ...], list[int, int]]:
        """
        Performs a normal roll of the dice.

        Args:
            modifier (int): Modifier to be added to the sum of the dice rolls.

        Returns:
            tuple: First element is a list of individual dice rolls.
                   Second element is a tuple with total sum after
                        adding the modifier and the modifier itself.
        """
        rolls: list[int, ...] = [self.die.roll() for _ in range(self.num_dice)]
        return rolls, [sum(rolls) + modifier, modifier]

    def exploding_roll(
            self, threshold: Optional[int] = None, modifier: int = 0
    ) -> tuple[list[int], list[int]]:
        """
        Performs an exploding roll where additional rolls are
            made for dice values above a threshold.

        Args:
            threshold (Optional[int]): Threshold value above which additional rolls are made.
            modifier (int): Modifier to be added to the sum of the dice rolls.

        Returns:
            tuple: Similar to normal_roll.
        """
        rolls: list[int, ...] = self.normal_roll(modifier)[0]
        threshold = self.die if threshold is None else threshold
        i = 0
        while i < len(rolls):
            if rolls[i] >= threshold:
                rolls.append(self.die.roll())
                i -= 1
            i += 1
        return rolls, [
            sum(roll for roll in rolls if isinstance(roll, int)) + modifier,
            modifier,
        ]

    def imploding_roll(
        self, threshold: Optional[int] = None, modifier: int = 0
    ) -> tuple[list[int], list[int]]:
        """
        Performs an imploding roll where additional rolls are
            made for dice values under a given threshold.

        Args:
            threshold (Optional[int]): Threshold value under which additional rolls are made.
            modifier (int): Modifier to be added to the sum of the dice rolls.

        Returns:
            tuple: First element is a list of individual dice rolls.
                   Second element is a tuple with total sum after
                        adding the modifier and the modifier itself.
        """
        rolls: list[int, ...] = self.normal_roll(modifier)[0]
        threshold = 1 if threshold is None else threshold
        i = 0
        while i < len(rolls):
            if rolls[i] <= threshold:
                rolls.append(self.die.roll())
            i += 1
        return rolls, [sum(rolls) + modifier, modifier]

    def drop_high(
        self, modifier: int = 0
    ) -> tuple[list[int, ...], list[int, int]]:
        """
        Performs a dice roll and drops the highest roll.

        Args:
            modifier (int): Modifier to be added to the sum of the dice rolls.

        Returns:
            tuple: First element is a list of individual dice rolls.
                   Second element is a tuple with total sum after
                        adding the modifier and the modifier itself.
        """
        rolls: list[int, ...] = self.normal_roll(modifier)[0]
        max_val = max(rolls)
        rolls[rolls.index(max_val)] = "DH"
        return rolls, [
            sum(roll for roll in rolls if isinstance(roll, int)) + modifier,
            modifier,
        ]

    def drop_low(
        self, modifier: int = 0
    ) -> tuple[list[int, ...], list[int, int]]:
        """
        Performs a dice roll and drops the lowest roll.

        Args:
            modifier (int): Modifier to be added to the sum of the dice rolls.

        Returns:
            tuple: First element is a list of individual dice rolls.
                   Second element is a tuple with total sum after
                        adding the modifier and the modifier itself.
        """
        rolls: list[int, ...] = self.normal_roll(modifier)[0]
        min_val = min(rolls)
        rolls[rolls.index(min_val)] = "DL"
        return rolls, [
            sum(roll for roll in rolls if isinstance(roll, int)) + modifier,
            modifier,
        ]

    def keep_high(
        self, modifier: int = 0
    ) -> tuple[list[int, ...], list[int, int]]:
        """
        Performs a dice roll and keeps only the highest roll.

        Args:
            modifier (int): Modifier to be added to the sum of the dice rolls.

        Returns:
            tuple: First element is a list of individual dice rolls.
                   Second element is a tuple with total sum after
                        adding the modifier and the modifier itself.
        """
        rolls: list[int, ...] = self.normal_roll(modifier)[0]
        max_val = max(rolls)
        rolls = ["KH" if roll != max_val else max_val for roll in rolls]
        return rolls, [
            sum(roll for roll in rolls if isinstance(roll, int)) + modifier,
            modifier,
        ]

    def keep_low(
        self, modifier: int = 0
    ) -> tuple[list[int, ...], list[int, int]]:
        """
        Performs a dice roll and keeps only the lowest roll.

        Args:
            modifier (int): Modifier to be added to the sum of the dice rolls.

        Returns:
            tuple: First element is a list of individual dice rolls.
                   Second element is a tuple with total sum after
                        adding the modifier and the modifier itself.
        """
        rolls: list[int, ...] = self.normal_roll(modifier)[0]
        min_val = min(rolls)
        rolls = ["KL" if roll != min_val else min_val for roll in rolls]
        return rolls, [
            sum(roll for roll in rolls if isinstance(roll, int)) + modifier,
            modifier,
        ]
