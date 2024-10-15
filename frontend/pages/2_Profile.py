import streamlit as st
import requests
import time

if 'Logged' not in st.session_state:
    st.session_state.Logged = True

greeting = """
Hello {Temp.name}, welcome back! Here, you can review and update your personal details, track your progress, and customize your experience.
We're glad to have you, and if there's anything you need to adjust, feel free to explore the options below.
"""

def response_generator():
    for word in greeting.split():
        yield word + " "
        time.sleep(0.05)


def Profile():
    st.set_page_config(page_title="Profile Page", page_icon="🕴️")
    st.title("User Profile:")
    with st.chat_message("assistant"):
        ############################
        # Get user Data and return #
        ############################
        st.write_stream(response_generator())

    _, col2, _ = st.columns([.4, .2, .4])

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
                #########################
                # Call user sign up api #
                #########################
                st.session_state.Logged = True
                st.rerun()
                pass
            else:
                st.error("Please fill out both fields.")

    with col2:
        st.header("Login")
        login_username = st.text_input("Enter your username", key="login_username")
        login_password = st.text_input("Enter your password", type="password", key="login_password")

        if st.button("Login"):
            if login_username and login_password:
                #################
                # Get user auth #
                #################
                st.session_state.Logged = True
                st.rerun()
                pass
            else:
                st.error("Please fill out both fields.")

if st.session_state.Logged:
    Profile()
else:
    Login()
    