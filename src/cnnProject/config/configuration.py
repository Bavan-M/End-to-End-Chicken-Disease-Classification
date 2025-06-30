import os
from cnnProject.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from cnnProject.utils.common import readYamlFile,createDirectories
from cnnProject.entity.config_entity import DataIngestionConfig,PrepareBaseModelConfig,TrainingConfig,EvaluationConfig
from pathlib import Path

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
    
    def get_prepare_base_model_config(self)->PrepareBaseModelConfig:
        config=self.config.prepare_base_model
        createDirectories([config.root_dir])
        prepare_base_model_config=PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_classes=self.params.CLASSES,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weight=self.params.WEIGHTS
        )
        return prepare_base_model_config
    
    def get_training_config(self)-> TrainingConfig:
        training=self.config.training
        prepare_base_model=self.config.prepare_base_model
        params=self.params
        training_data=os.path.join(self.config.data_ingestion.unzip_dir,"Chicken-fecal-images")
        createDirectories([Path(training.root_dir)])

        training_config=TrainingConfig(
            root_dir=Path(training.root_dir),
            trianed_model_path=Path(training.trianed_model_path),
            updated_base_model=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE,
        )

        return training_config
    
    def evaluation_config(self)-> EvaluationConfig:
        eval_config=EvaluationConfig(
            path_to_model='artifacts/training/model.h5',
            training_data='artifacts/data_ingestion/Chicken-fecal-images',
            mlflow_uri="https://dagshub.com/bavanreddy1999/End-to-End-Chicken-Disease-Classification.mlflow",
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
            )
        return eval_config