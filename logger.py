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

import json
import hashlib
import datetime
from typing import Optional, Union


class RollLogger:
    """
    Logs dice rolls and provides functionalities to access and manage the logs.

    Attributes:
        LOG_FILE (str): Name of the file where logs are stored.
        logs (list): List containing the logs.
    """

    LOG_FILE: str = "dice_rolls.json"

    def __init__(self) -> None:
        """
        Initializes a new instance of the Logger class and loads existing logs.
        """
        self.logs: list[
            dict[str, Union[str, list[str, str]]]
        ] = self.load_logs()

    def load_logs(self) -> list:
        """Loads the logs from the LOG_FILE.

        Returns:
            list: A list of logs. If the file is not found or corrupted,
                an empty list is returned.
        """
        try:
            with open(self.LOG_FILE, "r+", encoding='utf-8') as file:
                data = json.load(file)
                if isinstance(data, list):
                    return data
        except FileNotFoundError:
            return [f"File {self.LOG_FILE} not found."]
        except json.JSONDecodeError:
            return ["Error decoding JSON from the log file."]
        return []

    def save_logs(self) -> None:
        """
        Saves the current logs to the LOG_FILE.
        """
        with open(self.LOG_FILE, "w", encoding='utf-8') as file:
            json.dump(self.logs, file)

    def log_roll(self, roll_data: dict[str, str]) -> str:
        """
        Logs a new dice roll.

        Args:
            roll_data (dict): Data related to the dice roll.

        Returns:
            str: A unique hash generated based on the current timestamp,
                representing the logged roll.
        """
        current_time = datetime.datetime.now().isoformat()
        roll_hash = hashlib.md5(current_time.encode()).hexdigest()

        if len(self.logs) >= 500:
            self.logs.pop(0)
        self.logs.append(
            {"hash": roll_hash, "time": current_time, "roll_data": roll_data}
        )
        self.save_logs()
        return roll_hash

    def get_roll_by_hash(self, roll_hash: str) -> Optional[dict[str, str]]:
        """
        Retrieves a roll from the logs based on its hash.

        Args:
            roll_hash (str): The hash of the roll to be retrieved.

        Returns:
            dict: The roll data associated with the provided hash.
                None if the roll is not found.
        """
        for log in self.logs:
            if log["hash"] == roll_hash:
                return log["roll_data"]
        return None


class BotLogger:
    """
    BotLogger is used to log the timestamp of the bot last response.

    Attributes:
        timestamp_file (str): The name of the file where the timestamp
            of the last response is stored.
    """

    def __init__(
        self, timestamp_file: str = "last_response_timestamp.txt"
    ) -> None:
        """
        Initializes the BotLogger object with an optional file to store the timestamp.

        Args:
            timestamp_file (str), optional: name of the file to store the timestamp.
        """
        self.timestamp_file: str = timestamp_file

    def save_timestamp(self) -> None:
        """
        Saves the current timestamp to a file.

        Raises:
            IOError: If the file cannot be written to.
        """
        with open(self.timestamp_file, "w", encoding='utf-8') as file:
            file.write(str(datetime.datetime.now()))

    def get_last_timestamp(self) -> datetime.datetime:
        """
        Reads and returns the last timestamp from the file.

        Returns:
            datetime.datetime: The last timestamp from the file.
                If the file does not exist or has an invalid format,
                    it returns a timestamp representing 1900-01-01.
        Raises:
            IOError: If the file cannot be read from.
        """
        try:
            with open(self.timestamp_file, "r", encoding='utf-8') as file:
                last_timestamp = file.read().strip()
                return datetime.datetime.fromisoformat(last_timestamp)
        except (FileNotFoundError, ValueError):
            return datetime.datetime(year=1900, month=1, day=1)
