from cnnProject.config.configuration import ConfigurationManager
from cnnProject.components.prepare_base_model import PrepareBaseModel
from cnnProject import logger

STAGE_NAME="Prepare base Model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        prepare_base_model_config=config.get_prepare_base_model_config()
        prepare_base_model=PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()



if __name__=="__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj=PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f"stage >>>>>>> {STAGE_NAME} completed <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    
# It’s a special built-in variable in Python.
# -> When a Python file is run directly, __name__ is set to "__main__".
# -> When a Python file is imported as a module into another file, __name__ is set to the module’s name.

# True when you run the file directly:like python stage_02_prepare_base_model.py
#Then:
#__name__ == "__main__" ✅ becomes True
# -> Your pipeline runs:
# -> Logging starts
# -> PrepareBaseModelTrainingPipeline().main() is executed
# -> Logs success or exception

# False when the file is imported:
# -> Example : from cnnClassifier.pipeline import stage_02_prepare_base_model
# -> In this case:
# -> __name__ == "cnnClassifier.pipeline.stage_02_prepare_base_model" ❌
# -> So the block under if __name__ == "__main__": is not executed