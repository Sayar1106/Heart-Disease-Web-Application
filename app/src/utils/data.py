import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

def make_corr_plot(df):
    """
    Function to plot the correlation matrix.

    Parameters
    ----------
    df: DataFrame
        A dataframe containing the heart disease data.

    Returns
    -------
    fig: go.Figure 
       A figure object. 
    """
    # Plotly figure for creating correlation:
    fig = go.Figure(data=go.Heatmap(z=df.corr(), 
                                x=df.corr().columns, 
                                y=df.corr().columns, 
                                colorscale=px.colors.sequential.Blugrn, 
                                text=df.corr().values, 
                                ))

    # Updating the dimensions and title:
    fig.update_layout(height=600, 
                      width=600, 
                      title="Correlation Matrix Heatmap")
    
    return fig

def data(df):
    """Function for the data page in web app"""
    st.header("Viewing the dataset")
    # Check dimensions of data:
    st.markdown("""
                The dataset is comprised of {} rows and {} columns including the target variable.
                """.format(df.shape[0], df.shape[1]))
    #TODO(Sayar): Add checkbox here:
    # Read data:
    st.dataframe(data=df)
    st.subheader("Summary Table")
    st.write(df.describe())

    st.subheader("Data Description")
    st.markdown("""
                Here is a bit more fleshed out description of each variable:

                1. **age**: The person's age in years
                2. **sex**: The person's sex (1 = male, 0 = female)
                3. **cp**: The chest pain experienced (Value 1: typical angina, Value 2: atypical angina, Value 3: non-anginal pain, Value 4: asymptomatic)
                4. **trestbps**: The person's resting blood pressure (mm Hg on admission to the hospital)
                5. **chol**: The person's cholesterol measurement in mg/dl
                6. **bs**: The person's fasting blood sugar (> 120 mg/dl, 1 = true; 0 = false)
                7. **restecg**: Resting electrocardiographic measurement (0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy by Estes' criteria)
                8. **thalach**: The person's maximum heart rate achieved
                9. **exang**: Exercise induced angina (1 = yes; 0 = no)
                10. **oldpeak**: ST depression induced by exercise relative to rest ('ST' relates to positions on the ECG plot.)
                11. **slope**: the slope of the peak exercise ST segment (Value 1: upsloping, Value 2: flat, Value 3: downsloping)
                12. **ca**: The number of major vessels (0-3)
                13. **thal**: A blood disorder called thalassemia (3 = normal; 6 = fixed defect; 7 = reversable defect)
                14. **target**: Heart disease (0 = no, 1 = yes)
                """)

    st.subheader("Viewing correlations between the variables")
    st.plotly_chart(make_corr_plot(df))

