import pandas as pd
import streamlit as st
import base64
from clean_df import clean_df
""" filters import """
from date_range import date_range
from mag_filter import mag_filter

st.title('Earhquake data')

file = pd.read_csv('significant_month.csv')
file_df = pd.DataFrame(file)

def select_data(df):
    df = clean_df(df)
    columns = ['time', 'longitude', 'depth', 'mag', 'magSource', 'locationSource']
    new_df = df[columns]
    return new_df

selected_data = select_data(file_df)
""" FILTER PARAMETERS """

mags = selected_data.magSource.unique()
selected_source = mag_filter(mags)


st.sidebar.title("Date range")
dates = selected_data["time"].unique()
selected_start_date, selected_end_date = date_range(dates)


print('source s', selected_source)
new_selected_data = selected_data[(selected_data.magSource.isin(selected_source))
& (selected_data['time'] > selected_start_date)
& (selected_data['time'] < selected_end_date)]

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