
from textSummarizer.pipeline.stage_01_data_ingestion  import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
import os

from textSummarizer.logging import logger

STAGE_NAME = "data ingestion stage"
try:
   logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx======")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "data validation stage"
try:
   logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx======")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "data transformation stage"
try:
   logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx======")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "model training stage"
try:
   logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
   model_trainer = ModelTrainerTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx======")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "model evaluation stage"
try:
   logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.main()
   logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx======")
except Exception as e:
        logger.exception(e)
        raise e


