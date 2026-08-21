import streamlit as st
import requests

st.title("Student Pass Fail")

School = st.selectbox("School",["GP","MS"])

Sex = st.selectbox("Sex",["F","M"])

pstatus = st.selectbox("Pstatus",["T","A"])

Activities = st.selectbox("Activites",["yes","no"])

Study_time = st.number_input("Study Time(hrs)",min_value=0,max_value=300)

Failures = st.number_input("Failures",min_value=0,max_value=500)

Absences = st.number_input("Absences",min_value=0,max_value=200)

g1 = st.number_input("G1",min_value=0,max_value=90)

g2 = st.number_input("G2",min_value=0,max_value=90)


if st.button("Predict"):

    data = {"school":School,
            "sex":Sex,
            "Pstatus":pstatus,
            "activities":Activities,
            "studytime":Study_time,
            "failures":Failures,
            "absences":Absences,
            "G1":g1,
            "G2":g2}
    respose = requests.post( "https://student-p-f-status-using-fast-api.onrender.com/predict",
                            json=data)

    result = respose.json()

    if result["prediction"] == "Pass":
        st.sucess("Student Pass")
    else:
        st.error("student fail")