import os

import matplotlib.pyplot as mp
import pandas as pd
import pygwalker as pyg
import seaborn as sb
import streamlit as st
import streamlit.components.v1 as components
from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm

from src.files_reader import file_reader

#from src import files_reader

data_folder= "data"
files_names_list: list[str]= os.listdir(data_folder)

st.set_page_config(layout="wide")

st.sidebar.title("GUI-EDA")

data_file = st.sidebar.file_uploader("Upload file", type=["csv", "xlsx", "json"], help="Upload your data file here")

# Upload and Save the file
if data_file is not None:
        st.sidebar.write(f"{data_file.name} Uploaded Successfully!")
        if st.sidebar.button("Save File to Data Folder", ):
        # Create a directory if it doesn't exist
            os.makedirs("data", exist_ok=True)
        
        # Save the file to the data folder
            with open(os.path.join("data", data_file.name), "wb") as f:
                f.write(data_file.getvalue())
            st.sidebar.write("File saved successfully!")
        
# List all the Uploaded Files
st.sidebar.subheader("Uploaded Files are: ")   
if os.path.exists(data_folder):
    for files in files_names_list:
        delete_button_key = f"delete_{files}"
        if st.sidebar.button(f"Click to delete {files}", key=delete_button_key):
            os.remove(os.path.join(data_folder, files))
            st.sidebar.write(f"File '{files}' deleted successfully!")

#Select Box to u
selected_file = st.selectbox("Select File", files_names_list, )
st.write(f"You selected {selected_file}")
if selected_file:
    file_path = os.path.join(data_folder, selected_file)

    # Create an instance of FileReader
    reader = file_reader(file_path)

    # Read the file and get the DataFrame
    df = reader.read_file()

    # Display the head of the DataFrame
    st.header("Exploratory Data Analysis")
 
