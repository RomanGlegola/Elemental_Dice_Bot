import subprocess


class PipInstaller:

    @staticmethod
    def install_from_requirements(file_path="requirements.txt"):
        with open(file_path, 'r') as f:
            packages = f.readlines()
        for package in packages:
            subprocess.call(["pip", "install", package])