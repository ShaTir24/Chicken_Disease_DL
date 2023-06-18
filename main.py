from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline

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