import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from functions.utils import *
from functions.messages import *

def PreChat():
    st.set_page_config(page_title="Chad-Bot", page_icon="🕴️")

    st.title("Chad-Bot:")

    with st.chat_message("assistant"):
        st.write_stream(response_generator(F_chat))

def Chat():
    st.set_page_config(page_title="Chad-Bot", page_icon="🕴️")

    st.title("Chad-Bot:")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    if prompt := st.chat_input("Have something to Say?"):
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})
    
        response = "We will be right back to you."
        with st.chat_message("assistant"):
            response = st.write_stream(response_generator(response))
        st.session_state.messages.append({"role": "assistant", "content": response})

if 'Logged' not in st.session_state or st.session_state.Logged == False:
    st.session_state.Logged = False
    PreChat()
else:
    Chat()