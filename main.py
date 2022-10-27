import streamlit as st
from st_on_hover_tabs import on_hover_tabs


st.set_page_config(layout="wide")

st.header("HAR Course")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

with st.sidebar:
    
    tabs = on_hover_tabs(tabName=['Introduction to HAR', 'Working With HAR Data'], 
                         iconName=['dashboard', 'money'], default_choice=0)
