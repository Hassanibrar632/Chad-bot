import time
from sklearn.preprocessing import LabelEncoder
import streamlit as st
import pandas as pd
import numpy as np
import os
import io

USER_DATA_FILE = 'Data/users_data.csv'

def response_generator(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.15)

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

def df_info(df):
    buffer = io.StringIO ()
    df.info (buf=buffer)
    lines = buffer.getvalue().split('\n')
    list_of_list = []
    for x in lines [5:-3]:
        list = x.split ()
        list_of_list.append(list)
    info_df = pd.DataFrame(list_of_list, columns=['index', 'Column', 'Non-null-Count', 'null', 'Dtype'])
    info_df.drop(columns=['index'], axis=1, inplace=True)
    return info_df

def dataframe_with_selections(df_org, init_value=False):
    df = df_info(df_org)
    if 'df' not in st.session_state or st.session_state.df is None:
        st.session_state.df = df_org.copy()
    df_with_selections = df.copy()
    df_with_selections.insert(0, "Select", init_value)

    st.write("### Dataset info:")
    # Get dataframe row-selections from user with st.data_editor
    edited_df = st.data_editor(
        df_with_selections,
        hide_index=True,
        column_config={"Select": st.column_config.CheckboxColumn(required=True)},
        disabled=df.columns,
    )

    # Filter the dataframe using the temporary column, then drop the column
    selected_rows = edited_df[edited_df.Select]

    options = ['None']
    options.extend(['Label Encoder', 'Embbedings', 'Drop', 'Fillnan', 'Drop-NaN'])

    option = st.selectbox(
    "Select Preprocessing technique:",
    options,
    )

    c1, c2 = st.columns([.8, .2])

    with c1:
        if st.button('Process'):
            if option == 'Label Encoder':
                lb = LabelEncoder()
                for i in selected_rows['Column']:
                    try:
                        st.session_state.df[i]/2
                    except:
                        st.session_state.df[i] = lb.fit_transform(st.session_state.df[i])

            elif option == 'Drop':
                st.session_state.df.drop(selected_rows['Column'], axis=1, inplace=True)

            elif option == 'Drop-NaN':
                st.session_state.df.dropna(axis=0, how='any', inplace=True)

    with c2:
        if st.button('Reset'):
            st.session_state.df = None
    
    st.write("### Input Dataset Preview")
    try:
        st.dataframe(st.session_state.df)
    except:
        st.dataframe(pd.DataFrame({}))
