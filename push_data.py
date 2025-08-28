import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi 
ca=certifi.where()
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exceptionhandling.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def cv_to_json_converter(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)

            self.databse=self.mongo_client[self.database]
            self.collection=self.databse[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)

if __name__=='__main__':
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="Armaan"
    Collection="NetworkData"
    network_obj=NetworkDataExtract()
    records=network_obj.cv_to_json_converter(file_path=FILE_PATH)
    no_of_records=network_obj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)