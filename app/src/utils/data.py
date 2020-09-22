import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

def make_corr_plot(df):
    fig = go.Figure(data=go.Heatmap(z=df.corr(), 
                                x=df.corr().columns, 
                                y=df.corr().columns, 
                                colorscale=px.colors.sequential.Blugrn, 
                                text=df.corr().values, 
                                
                                ))
    fig.update_layout(height=600, 
                      width=600, 
                      title="Correlation Matrix Heatmap")
    
    return fig

def data(df):
    st.plotly_chart(make_corr_plot(df))

