import streamlit as st
import pandas as pd
import joblib

def create_inference_input(df):
    """
    Function that creates an input form for ML model.

    The function will build the structure for an input form
    using Streamlit functions. The input from the form will be
    taken and converted into a dictionary with the keys being
    the column names of the dataframe and the values being the 
    inputs.

    Parameters
    ----------
    df: DataFrame
        A dataframe containing the the heart disease data.
    
    Returns
    -------
    response_dict: Dict
        A dictionary containing the key, value pairs of the 
        column names of the dataframe and the values from the input
        form.
    """
    input_list = []
    age = st.sidebar.slider(label="Age", 
                            min_value=min(df["age"]), 
                            max_value=max(df["age"]))
    input_list.append(age)
    st.sidebar.write("\n")
    sex = st.sidebar.radio(label="Sex", 
                           options=df["sex"].unique().tolist())
    st.sidebar.write("\n")
    input_list.append(sex)
    chest_pain_type = st.sidebar.selectbox(label="Chest pain type", 
                                           options=df["chest_pain_type"].unique().tolist())
    st.sidebar.write("\n")
    input_list.append(chest_pain_type)
    resting_blood_pressure = st.sidebar.slider(label="Resting blood pressure mm Hg", 
                                               min_value=min(df["resting_blood_pressure"]), 
                                               max_value=max(df["resting_blood_pressure"]))
    st.sidebar.write("\n")
    input_list.append(resting_blood_pressure)
    cholesterol = st.sidebar.slider(label="Cholesterol measurement in mg/dl", 
                                    min_value=min(df["cholesterol"]),
                                    max_value=max(df["cholesterol"]))
    st.sidebar.write("\n")
    input_list.append(cholesterol)
    fasting_blood_sugar = st.sidebar.radio(label="Enter the range for the fasting blood sugar", 
                                           options=df["fasting_blood_sugar"].unique().tolist())
    st.sidebar.write("\n")
    input_list.append(fasting_blood_sugar)
    rest_ecg = st.sidebar.selectbox(label="Resting electromagnetic measurement.", 
                                        options=df["rest_ecg"].unique().tolist())
    st.sidebar.write("\n")
    input_list.append(rest_ecg)
    max_heart_rate_achieved = st.sidebar.slider(label="Maximum heart rate achieved",  
                                                min_value=min(df["max_heart_rate_achieved"]), 
                                                max_value=max(df["max_heart_rate_achieved"]))
    st.sidebar.write("\n")
    input_list.append(max_heart_rate_achieved)
    exercise_induced_angina = st.sidebar.radio(label="Exercise induced Angina?", 
                                               options=df["exercise_induced_angina"].unique().tolist())
    st.sidebar.write("\n")
    input_list.append(exercise_induced_angina)
    st_depression = st.sidebar.slider("Enter the ST depression during exercise", 
                                      min_value=min(df["st_depression"]), 
                                      max_value=max(df["st_depression"]))
    st.sidebar.write("\n")
    input_list.append(st_depression)
    st_slope = st.sidebar.selectbox(label="Slope of peak exercise ST segment", 
                                    options=df["st_slope"].unique().tolist())
    st.sidebar.write("\n")
    input_list.append(st_slope)
    num_major_vessels = st.sidebar.slider(label="Number of major vessels", 
                                          min_value=min(df["num_major_vessels"]), 
                                          max_value=max(df["num_major_vessels"]))
    st.sidebar.write("\n")
    input_list.append(num_major_vessels)
    thalassemia = st.sidebar.selectbox(label="History of Thalassemia?", 
                                       options=df["thalassemia"].unique().tolist())
    st.sidebar.write("\n")
    input_list.append(thalassemia)

    # Dictionary comprehension for creating the response dictionary:
    response_dict = {column:value for column, value in zip(df.columns, input_list)}

    return response_dict


def predictor(df):
    st.header("Machine Learning model predictor")
    st.write("""
             A **machine learning model** trained on the heart disease dataset will be used
             to predict whether a patient has heart disease or not. We will be providing dropdowns
             for the user to select inputs for different attributes. These will then be fed into
             the machine learning model which will help predict the possibility of heart disease or not.
             """)
    st.sidebar.header("Input form for ML model")
    # Getting user input values in correct format
    response_dict = create_inference_input(df)
    
    name = st.text_input(label="Enter your name")

    # Dump the user inputs in a file:
    if st.sidebar.button(label="Submit input to model"):
        joblib.dump(response_dict, "app/src/utils/payload_dump/response_dict.bin")

    if st.button(label="Predict"):
        # Load user inputs:
        response_dict = joblib.load("app/src/utils/payload_dump/response_dict.bin")
        # Append user inputs to existing dataframe:
        df = df.append(response_dict, ignore_index=True)
        # Load the saved ML model:
        model = joblib.load("app/src/models/rf_model.bin")
        # Drop the target variable:
        df.drop(["target"], axis=1, inplace=True)
        # Create dummy variables:
        df = pd.get_dummies(df, drop_first=True)
        # Get prediction:
        pred = model.predict(df.iloc[-1, :].values.reshape(1, -1))
        # Get the prediction probabilities for the two classes:
        pred_prob = model.predict_proba(df.iloc[-1, :].values.reshape(1, -1))
        # Convert prediction into human readable string:
        pred = "No you do not have heart disease" if pred == 0 else "You have heart disease"

        # Create a dataframe to store resutls:
        result = pd.DataFrame({"Values": [name, round(pred_prob[0][1], 2), pred]},
                                index=["Name", 
                                    "Probability of Heart Disease", 
                                    "Verdict"])
        st.write(result)


