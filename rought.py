import os

data_folder = "data"
files_names_list = os.listdir(data_folder) 


def file_extension():       #This function will give the file name only without extension
    
    list=[] 
    for file in files_names_list:
        split_tup = file.split(".")
        list.append(split_tup[1])
    return list 

for i in range(len(file_extension())):    
    if file_extension()[i] == "xlsx":
        print("csv")
    