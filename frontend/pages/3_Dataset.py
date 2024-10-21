import streamlit as st
import pandas as pd
import requests
import time

if 'df' not in st.session_state:
    st.session_state.df = None

greeting = """
To begin with dataset, please login to your account or register if you're new here. 
Once you're in, you'll have access to personalized data dashboard, and much more!
"""

def response_generator():
    for word in greeting.split():
        yield word + " "
        time.sleep(0.02)

def login_message():
    st.set_page_config(page_title="Dataset", page_icon="📊")
    st.title("Dataset Dashboard")
    with st.chat_message("assistant"):
        st.write_stream(response_generator())

def data_upload():
    st.set_page_config(page_title="Dataset Dashboard", page_icon="📊")
    ##########################
    #  Get dataset of users  #
    ##########################
    st.title("Select dataset from your history")
    # create a list of dataset from previous uploads

    st.title("Upload Your CSV Dataset")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    data_type = st.select_slider("Select the type of the Dataset", options=['Regression', 'Classification'])
    if uploaded_file is not None:
        name = uploaded_file.name
        df = pd.read_csv(uploaded_file)
        data_type = data_type
        user = st.session_state.user
        #########################
        # call API to save data #
        #########################
        
        st.success("File uploaded successfully!")
        st.rerun()

    else:
        st.info("Please upload a CSV file to proceed.")

def data_visulization():
    st.set_page_config(page_title="Dataset", page_icon="📊")
    st.title("Dataset Dashboard"):
    ########################################
    # Tab to dataset info for both dataset #
    ########################################
    # select the target column first

    ##########################
    # Tab to orignal dataset #
    ##########################

    #########################
    # Tab to edited dataset #
    #########################
    # select columns to display
    # perform operation on selected columns
    return

if st.session_state.logged:
    if st.session_state.df == None:
        data_upload()
    else:
        data_visulization()
else:
    login_message()


if 'Logged' not in st.session_state:
    st.session_state.Logged = False
    st.session_state.user = None