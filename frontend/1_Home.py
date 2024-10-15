import streamlit as st
import numpy as np
import time

greeting = """
Hello, and welcome! 👋
I’m your AI assistant, here to help streamline your work and boost productivity! Whether you're dealing with data analysis, visualizations, or building AI models, I can simplify the process for you. Here's how I can make your life easier:
Data Analysis & Visualization: I can quickly turn raw data into insightful, interactive graphs, helping you spot trends and make data-driven decisions in real time.
AI Model Training: No need to dive deep into code—simply provide your data, and I’ll help train AI models with just one click. Whether you're working with classification, regression, or clustering tasks, I’ve got you covered.
Real-Time Feedback: As you interact with your data and models, I provide real-time updates, allowing you to see changes instantly, iterate faster, and make smarter adjustments on the fly.
So, let’s get started! I’m here to handle the heavy lifting while you focus on creativity and strategy.
"""

def response_generator():
    
    for word in greeting.split():
        yield word + " "
        time.sleep(0.05)

def Home():
    st.set_page_config(page_title="Auto-AI", page_icon="🤖")

    st.title("Auto-AI")

    with st.chat_message("assistant"):
        st.write_stream(response_generator())
        st.bar_chart(np.random.randn(30, 3))

if 'Logged' not in st.session_state:
    st.session_state.Logged = False

Home()