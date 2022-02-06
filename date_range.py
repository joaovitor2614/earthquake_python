import streamlit as st

def date_range(dates):
    sorted_date = sorted(dates)
    selected_start_date = st.sidebar.selectbox('Start date', sorted_date)
    selected_end_date = st.sidebar.selectbox('End date', sorted_date)
    return selected_start_date, selected_end_date

