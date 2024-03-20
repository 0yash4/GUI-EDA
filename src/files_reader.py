#from src.logger import logging
from src.custom_exception import CustomException
import sys

import pandas as pd
import os

data_folder = "data"
files_names_list = os.listdir(data_folder)   #Gives the list of all the files available in data folder


#Below funtion will return the List[str] of file extension

class file_reader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        file_extension = os.path.splitext(self.file_path)[1].lower()
        if file_extension == ".csv":
            df = pd.read_csv(self.file_path)
        elif file_extension == ".json":
            df = pd.read_json(self.file_path)
        elif file_extension in [".xls", ".xlsx"]:
            df = pd.read_excel(self.file_path)
        else:
            raise ValueError("Unsupported file format")
        
#        logging.info(f"Read {self.file_path}")
        return df

            
    def head(self, files_names_list):
        pass
        





if __name__=="__main__":
    file_reader = file_reader()