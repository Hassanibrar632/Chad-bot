import streamlit as st
import requests
import time

if 'Logged' not in st.session_state:
    st.session_state.Logged = False
    st.session_state.user = 0

greeting = """
Hello Temp, welcome back! Here, you can review and update your personal details, track your progress, and customize your experience.
We're glad to have you, and if there's anything you need to adjust, feel free to explore the options below.
"""

def response_generator(name):
    temp = greeting.replace('Temp', name)
    for word in temp.split():
        yield word + " "
        time.sleep(0.02)

def Profile():
    st.set_page_config(page_title="Profile Page", page_icon="🕴️")
    temp = requests.get(url=f"http://127.0.0.1:8000/user/get/{st.session_state['user']}")
    data = temp.json()
    if data.get('result'):
        data = data.get('user')
        email = data['email']
        user = data['User']
        first_name = data['First_Name']
        last_name = data['Last_Name']

        st.title(f"{user} Profile: ")
        st.header(f"{email}")
        with st.chat_message("assistant"):
            st.write_stream(response_generator(f"{first_name} {last_name}"))

        _, col2, _ = st.columns([.4, .2, .4])

        with col2:
            if st.button("Log out"):
                st.session_state['user'] = False
                st.rerun()
    else:
        st.error(data.get('error'), icon="🚨")
def Login():
    st.set_page_config(page_title="Login Page", page_icon="🔒")

    col1, col2 = st.columns(2)

    with col1:
        st.header("Sign Up")
        sign_up_email = st.text_input("Enter email", key="sign_up_email")
        sign_up_first_name = st.text_input("Enter your First Name", key="sign_up_first_name")
        sign_up_last_name = st.text_input("Enter your Last Name", key="sign_up_last_name")
        sign_up_username = st.text_input("Choose a username", key="sign_up_username")
        sign_up_password = st.text_input("Choose a password", type="password", key="sign_up_password")
        confirm_password = st.text_input("Choose a password", type="password", key="confirm_password")
        if st.button("Sign Up"):
            if sign_up_password != confirm_password:
                st.error("Passwords do not match with each other.")
            elif sign_up_username and sign_up_password:
                payload = {
                    'email': sign_up_email,
                    'user': sign_up_username,
                    'FName': sign_up_first_name,
                    'LName': sign_up_last_name,
                    'Pass': sign_up_password
                }
                temp = requests.post(url=f"http://127.0.0.1:8000/user/create", json=payload)
                data = temp.json()
                if data.get('result'):
                    st.success(data.get('message'), icon="✅")
                else:
                    st.error(data.get('error'), icon="🚨")
            else:
                st.error("Please fill out both fields.")

    with col2:
        st.header("Login")
        login_username = st.text_input("Enter your username or email", key="login_username")
        login_password = st.text_input("Enter your password", type="password", key="login_password")

        if st.button("Login"):
            if login_username and login_password:
                payload = {
                    'user': login_username,
                    'Pass': login_password
                }
                temp = requests.post(url=f"http://127.0.0.1:8000/user/auth", json=payload)
                data = temp.json()
                if data.get('result'):
                    st.session_state.Logged = True
                    st.session_state.user = data.get('user')
                    st.rerun()
                else:
                    st.error(data.get('error'), icon="🚨")
            else:
                st.error("Please fill out both fields.")

if st.session_state.Logged:
    Profile()
else:
    Login()
    