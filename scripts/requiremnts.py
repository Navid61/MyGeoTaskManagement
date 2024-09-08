import subprocess
import sys
import importlib

# List of required packages
required_packages = [
    "requests",
    "python-dotenv",
    "pandas",
    "geopandas",
    "matplotlib",
    "numpy"
]

def check_and_install_packages(packages):
    for package in packages:
        try:
            importlib.import_module(package)
            print(f"{package} is already installed.")
        except ImportError:
            print(f"{package} is not installed. Installing now...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Check and install required packages
check_and_install_packages(required_packages)