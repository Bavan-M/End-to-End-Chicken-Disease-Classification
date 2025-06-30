from pathlib import Path
import tensorflow as tf
import mlflow
import mlflow.keras
from urllib.parse import urlparse
from cnnProject.entity.config_entity import EvaluationConfig
from cnnProject.utils.common import saveJSON
#model=tf.keras.models.load_model("artifacts/training/model.h5")
import dagshub
dagshub.init(repo_owner='bavanreddy1999', repo_name='End-to-End-Chicken-Disease-Classification', mlflow=True)
class Evaluation:
    def __init__(self,config:EvaluationConfig):
        self.config=config

    def _valid_generator(self):
        datagenerators_kwargs=dict(rescale=1./255,validation_split=0.30)
        dataflow_kwargs=dict(target_size=self.config.params_image_size[:-1],
                             batch_size=self.config.params_batch_size,
                             interpolation="bilinear")
        
        valid_datagenerator=tf.keras.preprocessing.image.ImageDataGenerator(**datagenerators_kwargs)

        self.valid_generator=valid_datagenerator.flow_from_directory(directory=self.config.training_data,subset="validation",shuffle=False,**dataflow_kwargs)

    @staticmethod
    def load_model(path:Path)-> tf.keras.Model:
        return tf.keras.models.load_model(path)
    
    def evaluation(self):
        self.model=self.load_model(self.config.path_to_model)
        self._valid_generator()
        self.score=self.model.evaluate(self.valid_generator)
    
    def save_score(self):
        scores={"loss":self.score[0],"accuracy":self.score[1]}
        saveJSON(path=Path("scores.json"),data=scores)

    def log_into_mlfow(self):
        mlflow.set_registry_uri(uri=self.config.mlflow_uri)
        tracking_uri_type_store=urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics({"loss":self.score[0],"accuracy":self.score[1]})

            if tracking_uri_type_store!="file":
                mlflow.keras.log_model(self.model,"model",registered_model_name="VGG16Model")
            else:
                mlflow.keras.log_model(self.model,"model")