import streamlit as st
import os

data_folder= "data"
files_names_list: list[str]= os.listdir(data_folder)

st.sidebar.title("GUI-EDA")
st.sidebar.subheader("Uploaded Files are: ")   
if os.path.exists(data_folder):
    for files in files_names_list:
        delete_button_key = f"delete_{files}"
        if st.sidebar.button(f"Click to delete {files}", key=delete_button_key):
            os.remove(os.path.join(data_folder, files))
            st.sidebar.write(f"File '{files}' deleted successfully!")