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

from logger import RollLogger
from roller import Roller


class DiceRollerApp:
    """
    A dice roller application that provides functionalities to roll
        dice with various options and reroll based on previous roll logs.

    Attributes:
        No public attributes.
    """

    def roll_dice(
        self,
        num_dice: int,
        sides: int,
        roll_type: str = "normal",
        modifier: int = 0,
        threshold: Optional[int] = None,
    ) -> tuple[int, int]:
        """
        Rolls dice based on the given parameters and logs the result.

        Args:
            num_dice (int): Number of dice to be rolled.
            sides (int): Number of sides on each dice.
            roll_type (str): Type of the roll. Default is "normal". (
                'normal' - default roll, 'e' - exploding, 'i' - imploding,
                'dh' - drop_high, 'dl' - drop_low, 'kh' - keep_high, 'kl' - keep_low).
            modifier (int): Modifier to be added to the sum of the dice rolls. Default is 0.
            threshold (int, optional): Threshold value for exploding or imploding rolls.

        Returns:
            tuple: First element contains the results of the dice roll.
                   Second element is the hash of the logged roll.

        Raises:
            ValueError: If the provided roll type is invalid.
        """
        roller = Roller(num_dice, sides)

        if roll_type == "normal":
            results = roller.normal_roll(modifier)
        elif roll_type == "e":
            results = roller.exploding_roll(modifier)
        elif roll_type == "i":
            results = roller.imploding_roll(modifier)
        elif roll_type == "dh":
            results = roller.drop_high(modifier)
        elif roll_type == "dl":
            results = roller.drop_low(modifier)
        elif roll_type == "kh":
            results = roller.keep_high(modifier)
        elif roll_type == "kl":
            results = roller.keep_low(modifier)
        else:
            raise ValueError("Invalid roll type")

        roll_data = {
            "type": roll_type,
            "num_dice": num_dice,
            "sides": sides,
            "modifier": modifier,
            "threshold": threshold,
            "results": results,
        }
        logger_instance = RollLogger()
        roll_hash = logger_instance.log_roll(roll_data=roll_data)

        return results, roll_hash

    def reroll_dice(self, roll_hash: str) -> tuple[int, int]:
        """
        Performs a reroll based on a previously logged roll using its hash.

        Args:
            roll_hash (str): The hash of the previously logged roll.

        Returns:
            tuple: Results of the reroll.

        Raises:
            ValueError: If the roll associated with the provided hash is not found.
        """
        logger_instance = RollLogger()
        roll_data = logger_instance.get_roll_by_hash(roll_hash)

        if not roll_data:
            raise ValueError("Roll not found")

        return self.roll_dice(
            roll_data["num_dice"],
            roll_data["sides"],
            roll_data["type"],
            roll_data["modifier"],
            roll_data["threshold"],
        )
