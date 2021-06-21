import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

def app():
    st.title('Tech Job Dashboard')

    st.write("The Alumni Resource Dashboard displays the trends of skills and employment in the tech industry. The data listed n this site was derived from Google Jobs API and we hope it’s useful in your job search and tech journey.")