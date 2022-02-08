import streamlit as st

def date_range(dates):
    sorted_date = sorted(dates)
    # get min and max values' indexes on avaliable dates """
    max_data_index = sorted_date.index(max(sorted_date))
    min_data_index = sorted_date.index(min(sorted_date))

    selected_start_date = st.sidebar.selectbox('Start date', sorted_date, index=min_data_index)
    selected_end_date = st.sidebar.selectbox('End date', sorted_date, index=max_data_index)
    return selected_start_date, selected_end_date

