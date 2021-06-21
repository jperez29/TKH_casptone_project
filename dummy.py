import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

data = pd.read_csv("datasets/updated_categories_employment_data.csv")

def app():
    st.title('Dummy page')

    ax = data[data["location_category"] == "atlanta georgia" ].groupby("job_category").size()
    # ax.set_title("Atlanta Tech Jobs")
    st.bar_chart(ax)