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

# Activate the virtual environment (this part is for informational purposes)
if os.name == 'nt':  # Windows
    activate_script = os.path.join(venv_path, "Scripts", "activate")
else:  # Linux/Mac
    activate_script = os.path.join(venv_path, "bin", "activate")

print(f"To activate the virtual environment, run: source {activate_script}")


