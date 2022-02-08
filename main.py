
import pandas as pd
import streamlit as st
import base64
from clean_df import clean_df
# import filters
from date_range import date_range
from mag_filter import mag_filter
# general functions
from filedownload import filedownload

st.title('Earhquake data')
# read file
file = pd.read_csv('significant_month.csv')
file_df = pd.DataFrame(file)

def select_data(df):
    # clean time data => convert to YYYY-MM-DD date format
    df = clean_df(df)
    # select desired columns from dataframe
    columns = ['time', 'longitude', 'depth', 'mag', 'magSource', 'locationSource']
    new_df = df[columns]
    return new_df



selected_data = select_data(file_df)
## FILTER PARAMETERS """
# magnitude source filter
mags = selected_data.magSource.unique()
selected_source = mag_filter(mags)


# date range filter
dates = selected_data["time"].unique()
selected_start_date, selected_end_date = date_range(dates)

# number of rows filter
num_of_earthquakes = st.sidebar.slider(
    'Number of earthquakes', 1, 7, value=len(selected_data.index)
)

## DATA SELECTION """
# selected data based on filters data
new_selected_data = selected_data[(selected_data.magSource.isin(selected_source))
& (selected_data['time'] > selected_start_date)
& (selected_data['time'] < selected_end_date)]

# limit rows based on number of earthquakes data filter
new_selected_data = new_selected_data[:num_of_earthquakes]

#plot dataframe
st.dataframe(new_selected_data)


# get download href
href = filedownload(new_selected_data)


## DOWNLOAD FILE"""
st.markdown(href, unsafe_allow_html=True)