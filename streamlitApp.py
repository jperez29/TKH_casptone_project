import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import about
import newyork
import newark
import atlanta
import losangeles
import home
import dummy


PAGES = {
    "Dummy": dummy,
    "Home": home,
    "Atlanta": atlanta,
    "Los Angeles": losangeles,
    "Newark": newark,
    "New York City": newyork,
    "About": about,
}

st.set_page_config(layout="wide")

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()




