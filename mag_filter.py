import streamlit as st

def mag_filter(mags):
    sorted_unique_source = sorted(mags)
    selected_source = st.sidebar.multiselect('Magnitude source',
    sorted_unique_source,
    sorted_unique_source)
    return selected_source