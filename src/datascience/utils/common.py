import os
import yaml
from src.datascience import logger
import json 
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml}loaded_successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError(f"Yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """
    Create list of directories
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory:{path}")


@ensure_annotations
def save_json(path_to_json:Path,data:dict):
    """
    Save json file
    """
    with open(path_to_json,"w") as json_file:
        json.dump(data,json_file,indent=4)
    
    logger.info(f"json file: {path_to_json} saved_successfully")

@ensure_annotations
def load_json(path_to_json:Path)->ConfigBox:
    """
    Load json file
    """
    with open(path_to_json) as f:
        content=json.load(f)

    logger.info(f"json file:{path_to_json}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any,path_to_bin:Path):
    """
    Save binary file
    """
    joblib.dump(data,path_to_bin)
    logger.info(f"binary file:{path_to_bin} saved_successfully")

@ensure_annotations
def load_bin(path_to_bin:Path)->Any:
    """
    Load binary file
    """
    data=joblib.load(path_to_bin)
    logger.info(f"binary file:{path_to_bin}")
    return data