import time
import streamlit as st
import pandas as pd
import os

def response_generator(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.15)

USER_DATA_FILE = 'users_data.csv'

def check_file():
    if not os.path.exists(USER_DATA_FILE):
        pd.DataFrame(columns=['username', 'password']).to_csv(USER_DATA_FILE, index=False)

def check_credentials(username, password):
    check_file()
    users = pd.read_csv(USER_DATA_FILE)
    for _, user in users.iterrows():
        if user['username'] == username and user['password'] == password:
            return True
    return False

def sign_up_user(username, password):
    check_file()
    users = pd.read_csv(USER_DATA_FILE)

    if username in users['username'].values:
        st.error("Username already exists. Please choose a different username.")
    else:
        new_user = pd.DataFrame({'username': [username], 'password': [password]})
        result = pd.concat([users, new_user], axis=0)
        result.to_csv(USER_DATA_FILE, index=False)
        st.success(f"User {username} registered successfully!")
