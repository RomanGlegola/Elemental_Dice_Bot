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
            file_path (str): Path to the requirements file (default is "requirements.txt").
        """
        with open(file_path, 'r') as f:
            packages = f.readlines()
        for package in packages:
            subprocess.call(["pip", "install", package])