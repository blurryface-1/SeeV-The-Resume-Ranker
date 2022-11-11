from pydoc import describe
from turtle import color
import matplotlib.colors as mcolors
import gensim
import gensim.corpora as corpora
from operator import index
from numpy import extract
from wordcloud import WordCloud
from pandas._config.config import options
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from PIL import Image
import time
import process as ps
import loadfile as lf


st.set_page_config(page_title="SeeV Resume Scorer", 
                    page_icon="Images//3-up.png")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.image('https://i.ibb.co/R9qP9fj/3.png', width=300)

st.markdown('<p><span class="subtitle">CV Ranker</span></p><br>', unsafe_allow_html=True)

st.sidebar.header('Data Customization')
st.sidebar.markdown('---')
if st.sidebar.button('Add Resumes'):
    if lf.docs_to_txt('a','Resume'):
        st.success('Added Successfully')
if st.sidebar.button('Reset Resumes'):
    if lf.docs_to_txt('w','Resume'):
        st.success('Reset Successfully')
st.sidebar.markdown('---')
if st.sidebar.button('Add Job Descriptions'):
    if lf.docs_to_txt('a','Job'):
        st.success('Added Successfully')
if st.sidebar.button('Reset Job Descriptions'):
    if lf.docs_to_txt('w','Job'):
        st.success('Reset Successfully')
st.sidebar.markdown('---')
if st.sidebar.button('Instant Resume Upload'):
    data = st.sidebar.file_uploader('Upload your resume here:', type=['pdf, docx, doc, txt, jpg, png'])
    # save it into the data folder
    if data is not None:
        st.write('Uploaded:', data)
        lf.save_file(data, './Data/Resumes/')
        st.success('Uploaded Successfully')
    else:
        st.write('No file selected.')
st.sidebar.markdown('---')

st.markdown('---')
jobs = lf.get_jobfiles()
if len(jobs) <= 1:
    st.markdown('<p><span class="describe"> There is only 1 Job Description present -",jobs[0],"Scores will be shown for this Job Description</span></p>', unsafe_allow_html=True)
else:
    st.write('<p><span class="describe"> There are {} Job Descriptions available. Please select one. </span></p>'.format(len(jobs)), unsafe_allow_html=True)

if len(jobs)>1:
    st.markdown('<p class="title1"> Choose Job Title: </p>', unsafe_allow_html=True)
    job = st.selectbox('',jobs)
    st.markdown('<p class="title2"> Job Description: </p>', unsafe_allow_html=True)
    st.text_area('',lf.load_job(job), height=200)

if st.button('Choose Job'):
    res = ps.get_similarity_list(job)
    score = ps.get_table(res)
    st.markdown('---')
    st.markdown('<p class="title2"> CVs Ranked: </p>', unsafe_allow_html=True)
    st.dataframe(score)
    st.markdown('---')
    # st.table(score)







