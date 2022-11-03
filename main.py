import streamlit as st
from st_on_hover_tabs import on_hover_tabs


st.set_page_config(layout="wide")

st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

#sidebar with tabs corresponding to lesson number
with st.sidebar:
    st.header("HARc")
    tabs = on_hover_tabs(tabName=['Background', 'Lesson 1: Intro', 'Lesson 2: Data', 'Lesson 3: Vis', 'Lesson 4: ML', 'Lesson 5: Apps'], 
                         iconName=['apps', 'looks_one', 'looks_two', 'looks_3', 'looks_4', 'looks_5'], default_choice=0)


if tabs == 'Background':
    ## background information on human activity recogntion
    st.header("📙 Background")
    st.markdown("""
    The Personal Health Informatics Lab (PHIRE) is a research laboratory at Temple Unversity aiming to understand
    people's quality of life needs and seemlessly assist through science and technology.
    This course aims to help students and researchers build the skills to help people through technology and specifically learn
    skills relevant to human activity recognition.""")
    st.image("https://sites.temple.edu/phire/files/2016/03/img002_600DPI-e1528386598899.jpg")


if tabs == 'Lesson 1: Intro':
    ## lesson 1: intro
    ## provide introductory information on using python for human activity recognition
    ## provide resource for trying HAR without coding (i.e. teachablemachine.com pose analysis)
    st.header("📝 1. Introduction into Human Activity Recogntion")
    st.markdown('HAR is the study that deals with identifying the specific movement or action of a person based on sensor data.') 
    st.image('https://cdn-images-1.medium.com/max/1600/1*9L__QC49eKx-MtwFw4f8Mg.png')


if tabs == 'Lesson 2: Data':
    ## lesson 2: data
    ## detailed lesson using python, pandas, and numpy to work with data
    st.header("📊 2. Data Analysis with Human Movement Data")
    st.markdown('Aditi enter text here!!')


if tabs == 'Lesson 3: Vis':
    ## lesson 3: vis
    ## detailed lesson on how to use plotly to visualize data (HAR data)
    st.header("📈 3. Visualization of Human Activity Data")
    st.markdown('Aditi enter text here!!')


if tabs == 'Lesson 4: ML':
    # lesson 4: ml
    ## detailed lesson on how to apply basic machine learning techniques
    st.header("🧠 4. Using Machine Learning to Predict Human Activity")
    st.markdown('Aditi enter text here!!')


if tabs == 'Lesson 5: Apps':
    #lesson 5: apps
    ## detailed lesson on how to build web apps to apply ML models and visualize data
    st.header("💻 5. Building Web Applications for Human Activity Recognition")
    st.markdown('Aditi enter text here!!')
