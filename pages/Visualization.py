import os

import pandas as pd
import pygwalker as pyg
import streamlit as st
import streamlit.components.v1 as components
from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm

from src.files_reader import file_reader

data_folder= "data"
files_names_list: list[str]= os.listdir(data_folder)

st.set_page_config(
     layout="wide"
)

st.sidebar.title("GUI-EDA")
st.sidebar.subheader("Uploaded Files are: ")
if os.path.exists(data_folder):
    for files in files_names_list:
        delete_button_key = f"delete_{files}"
        if st.sidebar.button(f"Click to delete {files}", key=delete_button_key):
            os.remove(os.path.join(data_folder, files))
            st.sidebar.write(f"File '{files}' deleted successfully!")
            
            
Selected_file = st.selectbox("Select File", files_names_list, index=None)
st.write(f"You selected {Selected_file}")
if Selected_file:
    file_path = os.path.join(data_folder, Selected_file)
    reader = file_reader(file_path)
    df = reader.read_file()
    
if Selected_file is not None:
    # Generate the HTML using Pygwalker
    pyg_html = pyg.to_html(df)
 
    # Embed the HTML into the Streamlit app
    components.html(pyg_html, height=850,)

