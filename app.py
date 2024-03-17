import streamlit as st 
import pandas as pd
import os
from src.logger import logging

st.sidebar.title("GUI-EDA")

data_file = st.sidebar.file_uploader("Upload file", type=["csv", "xlsx", "json"], help="Upload your data file here")

if data_file is not None:
    st.sidebar.write(f"{data_file.name} Uploaded Successfully!")
    if st.sidebar.button("Save File to Data Folder", key="save_button"):
        # Create a directory if it doesn't exist
        os.makedirs("data", exist_ok=True)
        
        # Save the file to the data folder
        with open(os.path.join("data", data_file.name), "wb") as f:
            f.write(data_file.getvalue())
        st.sidebar.write("File saved successfully!")