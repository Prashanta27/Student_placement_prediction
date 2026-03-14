import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("Student_placement_prediction.pkl", "rb"))

st.title("🎓 Student Placement Predictor")

cgpa = st.number_input("Enter Student CGPA", min_value=0.0, max_value=10.0)

if st.button("Predict Placement"):

    data = pd.DataFrame([[cgpa]], columns=["cgpa"])
    prediction = model.predict(data)

    if prediction[0] == 0:
        st.success("Result: Student Will Be Placed")
    else:
        st.error("Result: Student Will NOT Be Placed")