import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from PIL import Image

def app():
    # st.title('TKH Tech Employment Resource Dashboard')
    original_title = '<p style=" color:Blue; font-size: 50px;">TKH Tech Employment Resource Dashboard</p>'
    st.markdown(original_title, unsafe_allow_html=True)

    st.write("The Alumni Resource Dashboard seeks to facilitate an easier job search for fellows and alumni through analyzing, evaluating and visualizing data based on user needs and current economic and employment trends.")

    image = Image.open("lagos-techie-IgUR1iX0mqM-unsplash.jpg")
    st.image(image, use_column_width=True)

    st.write("The Alumni Resource Dashboard displays the trends of skills and employment in the tech industry. The data listed in this site was derived from Google Jobs API. We analyzed data for the following roles:")
    st.write("- Software Engineer")
    st.write("- Data Analyst")
    st.write("- Data Scientist")
    st.write("- Web Developer")
    st.write("- Front-end Developer")
    st.write("- Back-end Developer")
    st.write("- UX UI Designer")

    st.write("")
    st.write("")
    st.write("We hope it’s useful in your job search and tech journey!")
    

