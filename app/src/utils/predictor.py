import streamlit as st
import pandas as pd
import joblib

def create_inference_input(df):
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
    response_dict = create_inference_input(df)
    
    name = st.text_input(label="Enter your name")

    if st.sidebar.button(label="Submit input to model"):
        joblib.dump(response_dict, "app/src/utils/payload_dump/response_dict.bin")

    if st.button(label="Predict"):
        response_dict = joblib.load("app/src/utils/payload_dump/response_dict.bin")
        df = df.append(response_dict, ignore_index=True)
        model = joblib.load("app/src/models/rf_model.bin")
        df.drop(["target"], axis=1, inplace=True)
        df = pd.get_dummies(df, drop_first=True)
        pred = model.predict(df.iloc[-1, :].values.reshape(1, -1))
        pred_prob = model.predict_proba(df.iloc[-1, :].values.reshape(1, -1))
        pred = "No you do not have heart disease" if pred == 0 else "You have heart disease"

        result = pd.DataFrame({"Values": [name, round(pred_prob[0][1], 2), pred]},
                                index=["Name", 
                                    "Probability of Heart Disease", 
                                    "Verdict"])
        st.write(result)


