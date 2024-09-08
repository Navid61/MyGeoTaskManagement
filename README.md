### Note
Before do anything create a virtual environment and then install libraries on that,


### The script can check if the required components have already been installed.

```python
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
```

### Attention
Before running the code run setup.py file


# MyGeoTaskManagement
In this folder, I have added some scripts that can help me automate and manage geospatial data, as well as handle data between GeoServer and PostgreSQL


```zsh
POSTGRES_HOST=postgis
POSTGRES_PORT=5432
POSTGRES_DB=geoserver
POSTGRES_USERNAME=geoserve
POSTGRES_PASSWORD=geoserver
```