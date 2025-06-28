import urllib.request as request 
from cnnProject import logger
from cnnProject.utils.common import getSize
import zipfile
from cnnProject.entity.config_entity import DataIngestionConfig
from  pathlib import Path
import os

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
             filename,headers=request.urlretrieve(url=self.config.source_URL,filename=self.config.local_data_file)
             logger.info(f"{filename} downloaded Sucessfully with the  {headers} info")

        else:
            logger.info(f"file already exists of size {getSize(Path(self.config.local_data_file))}")
    
    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(name=unzip_path,exist_ok=True)
        with zipfile.ZipFile(file=self.config.local_data_file,mode='r') as zip_ref:
            zip_ref.extractall(unzip_path)
