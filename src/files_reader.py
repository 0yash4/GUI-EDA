from logger import logging


import pandas as pd
import os

data_folder = "data"
file_names = os.listdir(data_folder)


#function to read file name and extension


#Below funtion will return the List[str] of file extension
def file_extension():
    
    list=[] 
    for file in file_names:
        split_tup = file.split(".")
        list.append(split_tup[1])
    return list 
    

class file_reader():
    def __init__(self):
        os.makedirs(data_folder, exist_ok=True)
        for i in range(0, len(file_extension())):
            if file_extension()[i] == "csv":
                pd.read_csv(f"{data_folder}/{file_names[i]}")
                logging.info("Read CSV file")
                
        for i in range(0, len(file_extension())):
            if file_extension()[i] == "json":
                pd.read_json(f"{data_folder}/{file_names[i]}")
                logging.info("Read Json file")
                
a=file_reader()

