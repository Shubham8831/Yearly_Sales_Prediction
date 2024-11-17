import streamlit as st
import numpy as np
import pickle

with open("model/scaler.pkl","rb") as scaler_file:
    loaded_scaler = pickle.load(scaler_file)

with open("model/model.pkl","rb") as model_file:
    loaded_model = pickle.load(model_file)

st.title("Sales Predictor")
avg_session_length = st.number_input("Average Session Length (sec)")
time_on_app = st.number_input("Time on App (sec)")
length_of_membership = st.number_input("Length of Membership (year)")

if st.button("PREDICT"):
    data = np.array([avg_session_length, time_on_app, length_of_membership]).reshape(1,-1)
    data_new = loaded_scaler.transform(data)
    prediction = loaded_model.predict(data_new)


    st.success(f"Yearly Amount Spent is : Rs.{prediction[0]:.2f}")