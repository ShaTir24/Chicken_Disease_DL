import os
from pathlib import Path
import logging

#deciding what will be logged in the terminal
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')
#only the informational details and in time: message format

project_name = "cnnClassifier"
list_of_files = [
    ".github/workflows/.gitkeep",   #for deployment purpose, ignoring empty file changes across commits
    f"src/{project_name}/__init__.py",  #creating the src/cnnClassifier directory. The init files enables to directly perform import in any python file in the project
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)   #to make it compatible with windows paths as it contains '\'
    filedir, filename = os.path.split(filepath) #seperates directory and file name from path

    if filedir != "":   #creating a directory for a file
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")