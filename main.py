from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exceptionhandling.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import training_pipeline_config
import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=training_pipeline_config()
        DataIngestionConfig=DataIngestionConfig(trainingpipelineconfig)
        datavalidationconfig=DataValidationConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(DataIngestionConfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion_config()
        logging.info("data inititaion completed")
        print(dataingestionartifact)
        data_validation=DataValidation(dataingestionartifact,datavalidationconfig)
        logging.info("initiated the data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data validation completed")
        print(data_validation_artifact)
        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        logging.info("data transformation started")
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data transformation completed")

    except Exception as e:
           raise NetworkSecurityException(e,sys)