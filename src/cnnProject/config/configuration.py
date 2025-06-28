from cnnProject.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from cnnProject.utils.common import readYamlFile,createDirectories
from cnnProject.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,
                 config_file_path=CONFIG_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH):
        self.config=readYamlFile(config_file_path)
        self.params=readYamlFile(PARAMS_FILE_PATH)
        createDirectories([self.config.artifacts_root])

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config=self.config.data_ingestion
        createDirectories([config.root_dir])
        data_ingestion_config=DataIngestionConfig(root_dir=config.root_dir,source_URL=config.source_URL,local_data_file=config.local_data_file,unzip_dir=config.unzip_dir)
        return data_ingestion_config