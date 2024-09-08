import os
import sys
import subprocess

# Determine the home directory based on the operating system
home_dir = os.path.expanduser("~")
venv_path = os.path.join(home_dir, ".venv")

# Check if the .venv directory exists
if not os.path.exists(venv_path):
    print(f".venv directory not found in {home_dir}. Creating a new virtual environment...")
    
    # Create the virtual environment
    subprocess.run([sys.executable, "-m", "venv", venv_path])
    print(f"Virtual environment created at {venv_path}")
else:
    print(f".venv directory already exists in {home_dir}")

# Path to the requirements.txt file
requirements_file = "requirements.txt"

# Function to install packages from requirements.txt
def install_packages(venv_path, requirements_file):
    pip_executable = os.path.join(venv_path, "bin", "pip") if os.name != 'nt' else os.path.join(venv_path, "Scripts", "pip.exe")
    
    # Check if requirements.txt exists
    if os.path.exists(requirements_file):
        print(f"Installing packages from {requirements_file}...")
        subprocess.run([pip_executable, "install", "-r", requirements_file])
    else:
        print(f"{requirements_file} not found.")

# Install packages
install_packages(venv_path, requirements_file)


     
    

# Path to the requirements.txt file

