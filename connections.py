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

from nio import AsyncClient


class CredentialsManager:
    """
    Manages the process of loading credentials from a file.

    Methods:
        load_credentials: Load credentials from the specified file.
    """

    @staticmethod
    def load_credentials(file_path: str) -> dict[str, str]:
        """
        Load credentials from the given file path.

        The file should contain key-value pairs separated by a colon, e.g., "username: JohnDoe".
        Lines starting with "#" are ignored, allowing for comments in the credentials file.

        Args:
            file_path (str): Path to the credentials file.

        Returns:
            Dict[str, str]: A dictionary containing loaded credentials.

        Raises:
            ValueError: If "password" is not found in the credentials file.
        """
        credentials: dict = {}
        with open(file_path, "r", encoding='utf-8') as file:
            for line in file.readlines():
                if not line.strip().startswith("#") and ":" in line:
                    key, value = line.strip().split(":", 1)
                    credentials[key.strip()] = value.strip()
        if "password" not in credentials:
            raise ValueError("Password not found in the credentials file.")
        return credentials


class ClientFactory:
    """
    Creates instances of the AsyncClient using loaded credentials.

    Methods:
        create_client: Create an instance of AsyncClient.
    """

    @staticmethod
    def create_client() -> AsyncClient:
        """
        Create an instance of AsyncClient using credentials loaded from "credentials.txt".

        Returns:
            AsyncClient: An instance of AsyncClient.
        """
        credentials = CredentialsManager.load_credentials("credentials.txt")
        return AsyncClient(
            homeserver=credentials["homeserver"],
            user=credentials["username"],
            device_id=None,
        )
