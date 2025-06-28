import os
import yaml
from ensure import ensure_annotations
from pathlib import Path
from box import ConfigBox
from cnnProject import logger
from box.exceptions import BoxValueError
import json
from typing import Any
import joblib
import base64

@ensure_annotations
def readYamlFile(yaml_file_path:Path)-> ConfigBox:
    try:
        with open(file=yaml_file_path) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"the yaml file form the path {yaml_file_path} loaded Sucessfully")
            return ConfigBox(content)
    except BoxValueError :
        raise ValueError("the yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def createDirectories(path_to_directories:list,verbose=True):
    for path in path_to_directories:
        os.makedirs(name=path,exist_ok=True)
        if verbose :
            logger.info(f"Directories created Sucessfully at {path}")

@ensure_annotations
def saveJSON(path:Path,data:dict):
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"JSON file saved Sucessfully in the path {path}")

@ensure_annotations
def loadJSON(path:Path)-> ConfigBox:
    with open(path) as f:
        content=json.load(f)
    logger.info(f"the JSON file is read Sucessfully form the path {path}")
    return ConfigBox(content)

@ensure_annotations
def saveBin(data:Any,path:Path):
    joblib.dump(value=data,filename=path)
    logger.info(f"the binary file is saved in the path {path}")

@ensure_annotations
def loadBin(path:Path)-> Any:
    data=joblib.load(filename=path)
    logger.info(f"the binary file is read from the path {path}")
    return data

@ensure_annotations
def getSize(path:Path)-> str:
    size_KB=round(os.path.getsize(filename=path)/1024)
    return f"~{size_KB} KB"


def decodeImage(imgstring,filename):
    imgdata=base64.b64decode(imgstring)
    with open(filename,"wb") as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,"rb") as f:
        return base64.b64encode(f.read())