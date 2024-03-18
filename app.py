import streamlit as st 
import pandas as pd
import os

#from src import files_reader

data_folder= "data"
file_name: list[str]= os.listdir(data_folder)

st.sidebar.title("GUI-EDA")

data_file = st.sidebar.file_uploader("Upload file", type=["csv", "xlsx", "json"], help="Upload your data file here")

if data_file is not None:
        st.sidebar.write(f"{data_file.name} Uploaded Successfully!")
        if st.sidebar.button("Save File to Data Folder", ):
        # Create a directory if it doesn't exist
            os.makedirs("data", exist_ok=True)
        
        # Save the file to the data folder
            with open(os.path.join("data", data_file.name), "wb") as f:
                f.write(data_file.getvalue())
            st.sidebar.write("File saved successfully!")
        
 
st.sidebar.subheader("Uploaded Files are: ")   
if os.path.exists(data_folder):
    for files in file_name:
        delete_button_key = f"delete_{files}"
        if st.sidebar.button(f"Click to delete {files}", key=delete_button_key):
            os.remove(os.path.join(data_folder, files))
            st.sidebar.write(f"File '{files}' deleted successfully!")
            
Option = st.selectbox("Select File", file_name)
st.write(f"You selected {Option}")