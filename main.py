from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exceptionhandling.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import training_pipeline_config
import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=training_pipeline_config()
        DataIngestionConfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(DataIngestionConfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion_config()
        print(dataingestionartifact)

    except Exception as e:
           raise NetworkSecurityException(e,sys)