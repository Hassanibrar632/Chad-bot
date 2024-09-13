import streamlit as st
from utils import *
from messages import *
import numpy as np

def Home():
    st.set_page_config(page_title="Auto-AI", page_icon="🤖")

    st.title("Auto-AI")

    with st.chat_message("assistant"):
        st.write_stream(response_generator(greeting))
        st.bar_chart(np.random.randn(30, 3))

if 'Logged' not in st.session_state:
    st.session_state.Logged = False

Home()