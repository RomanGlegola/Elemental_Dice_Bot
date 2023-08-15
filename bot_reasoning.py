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

import re


class BotCommandParser:
    """
    A class to parse bot commands related to dice rolls.

    Attributes:
        dice_roll_pattern (re.Pattern): A compiled regex pattern to match
            dice roll commands.
        dice_reroll_pattern (re.Pattern): A compiled regex pattern to match
            dice reroll commands.
        ROLL_REGEX (re.Pattern): A compiled regex pattern to match
            '/roll' command.
        REROLL_REGEX (re.Pattern): A compiled regex pattern to match
            '/reroll' command with hexadecimal value.
    """

    ROLL_REGEX = re.compile(r"/roll")
    REROLL_REGEX = re.compile(r"/reroll ([a-fA-F0-9]+)")

    def __init__(self):
        """
        Initializes the BotCommandParser with a compiled regex pattern to
            match dice roll commands.
        """
        self.dice_roll_pattern = re.compile(
            r"/roll\s+(\d{1,3})d(\d{1,3})([\+\-]\d{1,3})?(dh|dl|kh|kl|e|i)?",
            re.IGNORECASE,
        )
        self.dice_reroll_pattern = re.compile(
            r"^(/reroll)\s(\w+)$", re.IGNORECASE
        )

    def parse_roll(self, text: str) -> dict or None:
        """
        Parse the provided text to extract dice roll components.

        Args:
            text (str): The text to parse.

        Returns:
            dict: A dictionary containing matched components or None if no match.
        """
        match = self.dice_roll_pattern.match(text)
        if match:
            groups = match.groups()
        return {
            "dice": groups[0] or 0,
            "sides": groups[1] or 0,
            "modifier": groups[2] or 0,
            "roll_type": groups[3] or "normal",
        }

    def parse_reroll(self, text: str) -> str or None:
        """
        Parse the provided text to extract reroll hash.

        Args:
            text(str): The text to parse.

        Returns:
            str: The extracted hash or None if no match.
        """
        match = self.dice_reroll_pattern.match(text)
        if match:
            groups = match.groups()
        return {
            "command": groups[0] or 0,
            "hash": groups[1] or 0,
        }
