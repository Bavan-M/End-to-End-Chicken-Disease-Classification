from cnnProject.config.configuration import ConfigurationManager
from cnnProject.components.evaluation import Evaluation 
from cnnProject import logger

STAGE_NAME="Evaluation stage"

class EvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config=ConfigurationManager()
        eval_config=config.evaluation_config()
        evaluation=Evaluation(config=eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        #evaluation.log_into_mlfow()

if __name__=="__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started")
        obj=EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

