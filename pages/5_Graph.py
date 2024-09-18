import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from functions.utils import *
from functions.messages import *
import matplotlib.pyplot as plt
import seaborn as sns


def Message_page():
    st.set_page_config(page_title="Graphy", page_icon="🕴️")

    st.title("Grapyh:")

    with st.chat_message("assistant"):
        st.write_stream(response_generator(G_chat))

def Graph_visulization():

    df = st.session_state.df

    st.set_page_config(page_title="Grapyh", page_icon="🕴️")

    st.title("Graphy:")
    
    if df[st.session_state.option].dtype == 'object' or df[st.session_state.option].nunique() <= 10:
        target_type = 'categorical'
    else:
        target_type = 'numerical'

    try:
        st.write("### Histograms for Numerical Columns")
        df.hist(figsize=(10, 8), bins=20)
        st.pyplot(plt.gcf())
    except Exception as e:
        st.error(f'Error: {e}', icon='🚨')

    try:
        st.write("### Correlation Heatmap")
        plt.figure(figsize=(12, 8))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
        st.pyplot(plt.gcf())
    except Exception as e:
        st.error(f'Error: {e}', icon='🚨')

    try:
        if target_type == 'categorical':
            st.write("### Violin Plot with Target Column")
            for col in df.columns:
                plt.figure(figsize=(8, 6))
                sns.violinplot(x=st.session_state.option, y=col, data=df)
                st.pyplot(plt.gcf())
    except Exception as e:
        st.error(f'Error: {e}', icon='🚨')
    
    try:
        st.write("### Count Plot for Categorical Columns")
        for col in df.columns:
            plt.figure(figsize=(8, 6))
            sns.countplot(x=col, data=df, hue=st.session_state.option if target_type == 'categorical' else None)
            st.pyplot(plt.gcf())
    except Exception as e:
        st.error(f'Error: {e}', icon='🚨')

    try:
        st.write("### Pairplot with Target Column")
        sns.pairplot(df, hue=st.session_state.option if target_type == 'categorical' else None)
        st.pyplot(plt.gcf())
    except Exception as e:
        st.error(f'Error: {e}', icon='🚨')

if 'df' not in st.session_state or st.session_state.df is None:
    st.session_state.df = None
    Message_page()
else:
    Graph_visulization()