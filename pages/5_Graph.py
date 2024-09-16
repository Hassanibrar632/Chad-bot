import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from functions.utils import *
from functions.messages import *
import pandas as pd

def Message_page():
    st.set_page_config(page_title="Graphy", page_icon="🕴️")

    st.title("Grapyh:")

    with st.chat_message("assistant"):
        st.write_stream(response_generator(G_chat))

def Graph_visulization():
    st.set_page_config(page_title="Grapyh", page_icon="🕴️")

    st.title("Graphy:")

    st.info("We have done That")



if 'df' not in st.session_state or st.session_state.df is None:
    st.session_state.df = None
    Message_page()
else:
    Graph_visulization()