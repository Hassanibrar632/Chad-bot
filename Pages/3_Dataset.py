import streamlit as st
from utils import *
from messages import *
import pandas as pd
import io

def data_visulization():

    col1, col2 = st.columns([.8, .2])
    with col1:
        st.title("Your CSV Dataset:")
    with col2:
        if st.button("Remove Dataset"):
            st.session_state.uploaded_file = False
            st.rerun()
    
    df = pd.read_csv(f'./Data/{st.session_state.uploaded_file}')
    st.dataframe(df.head())
    
    st.write("### Dataset info:")
    buffer = io.StringIO ()
    df.info (buf=buffer)
    lines = buffer.getvalue().split('\n')
    list_of_list = []
    for x in lines [5:-3]:
        list = x.split ()
        list_of_list.append(list)
    info_df = pd.DataFrame(list_of_list, columns=['index', 'Column', 'Non-null-Count', 'null', 'Dtype'])
    info_df.drop(columns=['index'], axis=1, inplace=True)
    st.dataframe(info_df)

    st.write("### Statistical Summary:")
    st.write(df.describe())

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
