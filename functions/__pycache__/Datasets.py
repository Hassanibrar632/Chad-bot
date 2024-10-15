import streamlit as st
import pandas as pd
import io

class Dataset():
    def __init__(self, path):
        self.df = pd.read_csv(path)

    def discribe_data(self):
        st.dataframe(self.df.head())

        st.write("### Missing Values")
        st.write(self.df.isnull().sum())

        st.write("### Statistical Summary:")
        st.write(self.df.describe())

    def df_info(self):
        buffer = io.StringIO ()
        self.df.info (buf=buffer)
        lines = buffer.getvalue().split('\n')
        list_of_list = []
        for x in lines [5:-3]:
            list = x.split ()
            list_of_list.append(list)
        info_df = pd.DataFrame(list_of_list, columns=['index', 'Column', 'Non-null-Count', 'null', 'Dtype'])
        info_df.drop(columns=['index'], axis=1, inplace=True)
        return info_df
    
    def dataframe_with_selections(self, init_value=False):
        temp = self.df_info()
        self.processed_df = temp.copy()
        self.processed_df.insert(0, "Select", init_value)

        st.write("### Dataset info:")
        # Get dataframe row-selections from user with st.data_editor
        edited_df = st.data_editor(
            self.processed_df,
            hide_index=True,
            column_config={"Select": st.column_config.CheckboxColumn(required=True)},
            disabled=temp.columns,
        )

        # Filter the dataframe using the temporary column, then drop the column
        self.processed_df = edited_df[edited_df.Select]