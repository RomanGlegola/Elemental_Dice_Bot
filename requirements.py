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

import subprocess


class PipInstaller:
    """
    A class to facilitate the installation of Python packages using pip.

    Methods:
        install_from_requirements(file_path="requirements.txt"):
            Installs packages listed in a requirements file.
    """

    @staticmethod
    def install_from_requirements(file_path: str = "requirements.txt"):
        """
        Install packages listed in a requirements file using pip.

        Args:
            file_path (str): Path to the requirements file,
                default is "requirements.txt".
        """
        with open(file_path, "r", encoding='utf-8') as file:
            packages = file.readlines()
        for package in packages:
            subprocess.call(["pip", "install", package])

if __name__ == "__main__":
    PipInstaller.install_from_requirements()
