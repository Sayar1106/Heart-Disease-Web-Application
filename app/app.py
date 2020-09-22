import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import os
from src.utils.data import data
from src.utils.home import home


PAGE_DICT = {"Home": home,
             "Data": data,
             "Visualizations": None,
             "Heart Disease Predictor": None
            }

def main():
    st.title("Heart Disease Application")
    df = pd.read_csv("app/src/data/heart.csv")
    option = st.sidebar.radio(label="Menu", 
                             options=["Home", 
                                     "Data", 
                                     "Visualizations", 
                                     "Heart Disease Predictor"])

    PAGE_DICT[option](df)

if __name__ == "__main__":
    main()