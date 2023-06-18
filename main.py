from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from cnnClassifier.pipeline.stage_03_training import TrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage: {STAGE_NAME} started! <<<<<<")
    obj = DataIngestionTrainPipeline()
    obj.main()
    logger.info(f">>>>>> Stage: {STAGE_NAME} completed! <<<<<<\n\nx===============x")
except Exception as e:
    raise e

STAGE_NAME = "Preparing Base Model Stage"
try:
    logger.info(f">>>>>> Stage: {STAGE_NAME} started! <<<<<<")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f">>>>>> Stage: {STAGE_NAME} completed! <<<<<<\n\nx===============x")
except Exception as e:
    raise e

STAGE_NAME = "Training Model Stage"
try:
    logger.info(f">>>>>> Stage: {STAGE_NAME} started! <<<<<<")
    obj = TrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage: {STAGE_NAME} completed! <<<<<<\n\nx===============x")
except Exception as e:
    raise e

STAGE_NAME = "Evaluating Model Stage"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e