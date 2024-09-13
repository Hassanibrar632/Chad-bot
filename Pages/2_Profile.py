import streamlit as st
from utils import *
from messages import *

def Profile():
    st.set_page_config(page_title="Profile Page", page_icon="🕴️")
    
    col1, col2 = st.columns([.8, .2])
    
    with col1:
        st.title("User Profile:")

        with st.chat_message("assistant"):
            temp = P_greeting.replace('Temp.name', st.session_state.user_name)
            st.write_stream(response_generator(temp))
    with col2:
        if st.button("Log out"):
            st.session_state.Logged = False
            st.rerun()

def Login():
    st.set_page_config(page_title="Login Page", page_icon="🔒")

    col1, col2 = st.columns(2)

    with col1:
        st.header("Sign Up")
        sign_up_username = st.text_input("Choose a username", key="sign_up_username")
        sign_up_password = st.text_input("Choose a password", type="password", key="sign_up_password")
        confirm_password = st.text_input("Choose a password", type="password", key="confirm_password")
        if st.button("Sign Up"):
            if sign_up_password != confirm_password:
                st.error("Passwords do not match with each other.")
            elif sign_up_username and sign_up_password:
                sign_up_user(sign_up_username, sign_up_password)
            else:
                st.error("Please fill out both fields.")

    with col2:
        st.header("Login")
        login_username = st.text_input("Enter your username", key="login_username")
        login_password = st.text_input("Enter your password", type="password", key="login_password")

        if st.button("Login"):
            if login_username and login_password:
                if check_credentials(login_username, login_password):
                    st.success(f"Welcome back, {login_username}!")
                    time.sleep(0.15)
                    st.session_state.Logged = True
                    st.session_state.user_name = login_username
                    st.rerun()
                else:
                    st.error("Invalid username or password.")
            else:
                st.error("Please fill out both fields.")

if 'Logged' not in st.session_state or st.session_state.Logged == False:
    st.session_state.Logged = False
    Login()
else:
    Profile()
