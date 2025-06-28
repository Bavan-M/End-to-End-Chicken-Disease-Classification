
from cnnProject.config.configuration import ConfigurationManager
from cnnProject.components.data_ingestion import DataIngestion
from cnnProject import logger

STAGE_NAME="Data Ingestion Stage"
class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingetion=DataIngestion(config=data_ingestion_config)
        data_ingetion.download_file()
        data_ingetion.extract_zip_file()
        