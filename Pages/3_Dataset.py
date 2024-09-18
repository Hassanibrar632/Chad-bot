import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from functions.utils import *
from functions.messages import *
import pandas as pd

def data_visulization():
    st.set_page_config(page_title="Upload Dataset", page_icon="📊")

    col1, col2 = st.columns([.8, .2])
    with col1:
        st.title("Your CSV Dataset:")
    with col2:
        if st.button("Remove Dataset"):
            st.session_state.uploaded_file = False
            st.session_state.df = None
            st.rerun()

    df = pd.read_csv(f'./Data/{st.session_state.uploaded_file}')
    options = ['None']
    options.extend(df.columns)

    index = 0
    try:
        if 'option' in st.session_state and st.session_state.option != ['None']:
            index = options.index(st.session_state.option)
    except:
        pass

    option = st.selectbox(
    "Select Prediction Cloumn:",
    options, index=index
    )

    if option == 'None':
        st.warning("Warning: Please setect the Target column.", icon="🚨")

    
    st.session_state.option = option
    
    st.dataframe(df.head())

    st.write("### Missing Values")
    st.write(df.isnull().sum())

    st.write("### Statistical Summary:")
    st.write(df.describe())

    try:
        dataframe_with_selections(df)
    except Exception as e:
        st.warning(f'Error {e}', icon='🚨')

def data_upload():
    st.set_page_config(page_title="Upload Dataset", page_icon="📊")

    st.title("Upload Your CSV Dataset")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        st.session_state.uploaded_file = uploaded_file.name
        temp = pd.read_csv(uploaded_file)
        temp.to_csv(f"Data/{uploaded_file.name}", index_label=False)
        st.success("File uploaded successfully!")
        st.rerun()

    else:
        st.info("Please upload a CSV file to proceed.")


if 'uploaded_file' not in st.session_state or st.session_state.uploaded_file == False:
    st.session_state.uploaded_file = False
    data_upload()
else:
    data_visulization()
