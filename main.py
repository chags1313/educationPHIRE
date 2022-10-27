import streamlit as st
from st_on_hover_tabs import on_hover_tabs


st.set_page_config(layout="wide")

st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

with st.sidebar:
    st.header("HARc")
    tabs = on_hover_tabs(tabName=['Background', 'Lesson 1: Intro', 'Lesson 2: Data', 'Lesson 3: Vis', 'Lesson 4: ML', 'Lesson 5: Apps'], 
                         iconName=['apps', 'looks_one', 'looks_two', 'looks_3', 'looks_4', 'looks_5'], default_choice=0)
if tabs == 0:
    ## background information on human activity recogntion
    st.header("📙 Background")
if tabs == 1:
    ## lesson 1: intro
    ## provide introductory information on using python for human activity recognition
    ## provide resource for trying HAR without coding (i.e. teachablemachine.com pose analysis)
    st.header("📝 1. Introduction into Human Activity Recogntion")
if tabs == 2:
    ## lesson 2: data
    ## detailed lesson using python, pandas, and numpy to work with data
    st.header("📊 2. Human Movement Data")
if tabs == 3:
    ## lesson 3: vis
    ## detailed lesson on how to use plotly to visualize data (HAR data)
    st.header("📈 3. Visualization of Human Activity Data")
if tabs == 4:
    # lesson 4: ml
    ## detailed lesson on how to apply basic machine learning techniques
    st.header("🧠 4. Using Machine Learning to Predict Human Activity")
if tabs == 5:
    #lesson 5: apps
    ## detailed lesson on how to build web apps to apply ML models and visualize data
    st.header("💻 5. Building Web Applications for Human Activity Recognition")
