# By Tushar Aggarwal

# Importing the required libraries
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Application title and body
st.set_page_config(page_title="Supermarket Sales Dashboard",
                   page_icon=":🏈:",
                   layout='wide')
# Title
st.title("NFL Stats (Rushing)")
st.write("By Tushar Aggarwal")

st.markdown("""
This application performs webscraping of NFL football player data(focusing on Rushing)!
* **Data Source:**[pro-football-reference.com](https://www.pro-football-reference.com/)
""")

# Side Panel
