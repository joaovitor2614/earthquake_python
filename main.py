import pandas as pd
import streamlit as st
import base64

st.title('Earhquake data')

file = pd.read_csv('significant_month.csv')
file_df = pd.DataFrame(file)

def select_data(df):
    columns = ['longitude', 'depth', 'mag', 'magSource', 'locationSource']
    new_df = df[columns]
    return new_df

selected_data = select_data(file_df)
""" filters parameters """

sorted_unique_source = sorted(selected_data.magSource.unique())
selected_source = st.sidebar.multiselect('Magnitude source', sorted_unique_source, sorted_unique_source)


new_selected_data = selected_data[(selected_data.magSource.isin(selected_source))]
num_of_earthquakes = st.sidebar.slider(
    'Number of earthquakes', 1, 7, value=len(new_selected_data.index)
)
new_selected_data = new_selected_data[:num_of_earthquakes]
st.dataframe(new_selected_data)

def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
    return href


st.markdown(filedownload(new_selected_data), unsafe_allow_html=True)