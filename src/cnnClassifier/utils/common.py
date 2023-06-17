import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

"""
ConfigBox is used to display the value of key in a dict using d.key syntax.
Normally, we should access like: d['key'] which is inconvinient.
Just pass the dict data of key value pairs in the args of ConfigBox method.
"""

"""
Ensure Annotations decorator is used to restrict the use of only the specified
data type that is mentioned in the arguments of the function while defining
"""

#function to read yaml files
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml files and returns
    
        Args:
            path_to_yaml(str): path to yaml file like input
            
        Raises:
            ValueError: if yaml file is empty
            e: empty files
        
        Returns:
            ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully!")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
#function to create directories with specified paths
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
        create a list of directories
        Args: 
            list of path to directories
            ignore_log (bool, optional): ignore if multiple dires is to be created. Defaults to False
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

#function to save the data in json format
#the data is related to model evaluation metrices involving loss and accuracy values
@ensure_annotations
def save_json(path: Path, data: dict):
    """saves the data in json format
    
        Args:
            path_to_json(str): path to json file like input
            data(Any): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

#function to load any json file
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data
    
        Args:
            path(str): path to json file like input
        
        Returns:
            ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

#function to save file in binary format
@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file
        Args:
            data (any): data to be saved as binary
            path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

#function to load the binary file
@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data
    Args:
        path(Path): path to binary file
    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

#function to obtain file size
@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    Args:
        path(Path): path to the file
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

#function to decode the base64 string into image data
def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

#function to encode the image into string base64
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
    
