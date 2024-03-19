from logger import logging
from custom_exception import CustomException
import sys

import pandas as pd
import os

data_folder = "data"
files_names_list = os.listdir(data_folder)   #Gives the list of all the files available in data folder


#Below funtion will return the List[str] of file extension

def file_nameOnly():   #This function will give the file name only without extension
    
    list=[] 
    for file in files_names_list:
        split_tup = file.split(".")
        list.append(split_tup[0])
    return list 

def file_extension():       #This function will give the file name only without extension
    
    list=[] 
    for file in files_names_list:
        split_tup = file.split(".")
        list.append(split_tup[1])
    return list 

class file_reader():
    def __init__(self):
            os.makedirs(data_folder, exist_ok=True)
            for i in range(0, len(file_extension())):
                if file_extension()[i] == "csv":
                    pd.read_csv(f"{data_folder}/{files_names_list[i]}")
                    logging.info(f"Read {files_names_list[i]}")

                elif file_extension()[i] == "json":
                    pd.read_json(f"{data_folder}/{files_names_list[i]}")
                    logging.info(f"Read {files_names_list[i]}")
                
                else:    
                    pd.read_excel(f"{data_folder}/{files_names_list[i]}")
                    logging.info(f"Read {files_names_list[i]}")

            
    def head(self, files_names_list):
        pass
        





if __name__=="__main__":
    file_reader = file_reader()