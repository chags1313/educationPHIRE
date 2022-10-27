import streamlit as st
from st_on_hover_tabs import on_hover_tabs


st.set_page_config(layout="wide")

st.header("HAR Course")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

with st.sidebar:
    
    tabs = on_hover_tabs(tabName=['Lesson 1: Intro', 'Lesson 2: Data', 'Lesson 3: Visualization', 'Lesson 4: ML', 'Lesson 5: Apps'], 
                         iconName=['dashboard', 'money', 'chart', 'brain', 'apps'], default_choice=0)
