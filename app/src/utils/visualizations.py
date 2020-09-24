import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import time

def plot_single_feature(df, feature):
    fig = None
    xaxis_type=None
    yaxis_title=""

    df["num_major_vessels"] = df["num_major_vessels"].astype("object")
    df["target"] = df["target"].astype("object")
    if df[feature].dtype == 'int64' or df[feature].dtype == 'float64':
        #TODO(Sayar) Add slider widget here:
        fig = px.histogram(x=df[feature].values, nbins=0)

        yaxis_title = "Frequency"

    elif df[feature].dtype == 'object':
        fig = px.bar(y=df[feature].value_counts(), 
                     x=df[feature].value_counts().index.astype(str), 
                     color=df[feature].value_counts().index.astype(str), 
                     text=df[feature].value_counts())

        xaxis_type = "category"
        yaxis_title = "Count"

    fig.update_xaxes(title=feature)
    fig.update_yaxes(title=yaxis_title)
    fig.update_layout(showlegend=False,
                      height=500, 
                      width=500, 
                      title="Distribution of {}".format(feature), 
                      xaxis_type=xaxis_type)

    st.plotly_chart(fig)
    return 

def plot_numerical_numerical(df, feature_1, feature_2):
    fig = px.scatter(df, feature_1, feature_2)
    fig.update_layout(title="Plot of {} vs. {}".format(feature_1, 
                                                       feature_2))

    st.plotly_chart(fig)

def plot_numerical_categorical(df, feature_1, feature_2):
    x_var,y_var = feature_1, feature_2
    if df[feature_1].dtypes == "int64" or df[feature_1].dtypes == "float64":
        x_var,y_var = y_var,x_var
    fig = px.box(df, 
                 x=x_var, 
                 y=y_var, 
                 color=x_var
                 )
    fig.update_layout(title="Plot of {} vs. {}".format(x_var, y_var))

    st.plotly_chart(fig)

def plot_categorical_categorical(df, feature_1, feature_2):
    fig = px.parallel_categories(df, 
                                 dimensions=[feature_1, feature_2], 
                                 )
    fig.update_layout(title="Plot of {} vs. {}".format(feature_1, feature_2))

    st.plotly_chart(fig)

def plot_dual_features(df, feature_1, feature_2):

    if feature_1 == feature_2:
        raise ValueError("Please select two different features.")
    df["num_major_vessels"] = df["num_major_vessels"].astype("object")
    df["target"] = df["target"].astype("object")
    feature_1_type = str(df[feature_1].dtype)
    feature_2_type = str(df[feature_2].dtype)

    switch_dict = {
        ("int64", "float64"): plot_numerical_numerical, 
        ("float64", "int64"): plot_numerical_numerical,
        ("float64", "float64"): plot_numerical_numerical,
        ("int64", "int64"): plot_numerical_numerical,
        ("int64", "object"): plot_numerical_categorical,
        ("float64", "object"): plot_numerical_categorical,
        ("object", "int64"): plot_numerical_categorical,
        ("object", "float64"): plot_numerical_categorical,
        ("object", "object"): plot_categorical_categorical
    }

    switch_dict[(feature_1_type, feature_2_type)](df, feature_1, feature_2)

    return


def visualizations(df):
    st.header("Visualizing our data")
    column_list = df.columns.to_list()
    st.markdown("""
            This section will have visualizations which will be created automatically
            based on rules assigned for the type of variable being visualized. 

            Rules for single variable visualizations:
            * Numerical variables will be represented by histograms.
            * The visualizations for numerical variables will have "Frequency" as the y-axis label.
            * Categorical variables will be represented by bar charts.
            * The visualizations for categorical variables will have "Count" as the y-axis label. 
            """)


    st.subheader("Single feature visualization")
    feature = st.selectbox(label="Select the feature", options=column_list)
    plot_single_feature(df, feature)

    st.markdown("""
                Feature interaction visualizations will have two variables
                and will plot the relationship between them.

                Rules for feature interaction visualization:
                * Only two variables can be used for this visualization.
                * Both variables have to be different.
                * For numerical vs numerical visuals, we will be using scatter plots.
                * For numerical vs categorical visuals, we will be using box plots.
                * For categorical vs categorical visuals, we will be using scatter plots.
                """)

    st.subheader("Feature interaction visualization")
    features = st.multiselect(label="Select any two distinct features", 
                              options=column_list)
    if len(features) == 2:
        plot_dual_features(df, features[0], features[1])

