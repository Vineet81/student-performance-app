import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

# Load model and columns
model = pickle.load(open("student_model.pkl", "rb"))
sample_df = pd.read_csv("prediction.csv")  # For column names
columns = list(sample_df.columns)

st.title("🎓 Student Performance Predictor (G3)")

# Sidebar selection
option = st.sidebar.selectbox("Select Mode", ("Single Input", "Bulk Input", "Visualization"))

# Function to preprocess input
def preprocess_input(data):
    return pd.DataFrame([data])

# Single input mode
if option == "Single Input":
    st.subheader("📌 Single Student Input")
    user_input = {}
    for col in columns:
        user_input[col] = st.number_input(f"{col}", value=0)
    
    if st.button("Predict"):
        input_df = preprocess_input(user_input)
        result = model.predict(input_df)[0]
        st.success(f"🎯 Predicted Final Grade (G3): {round(result, 2)}")

# Bulk input mode
elif option == "Bulk Input":
    st.subheader("📤 Bulk CSV Upload")
    uploaded_file = st.file_uploader("Upload a CSV file with input features", type=["csv"])
    
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("📄 Uploaded Data:")
        st.dataframe(data.head())

        predictions = model.predict(data)
        data["Predicted_G3"] = predictions
        st.write("✅ Predictions:")
        st.dataframe(data)

        # Download button
        csv = data.to_csv(index=False).encode('utf-8')
        st.download_button("Download Predictions", csv, "predictions_with_g3.csv", "text/csv")

# Visualization
else:
    st.subheader("📊 Actual vs Predicted Visualization")
    
    if st.checkbox("Use Test Sample (25 Records)"):
        predictions = model.predict(sample_df)
        actuals = pd.read_csv("student-mat.csv", sep=";")["G3"].iloc[sample_df.index]
        
        plt.figure(figsize=(8,5))
        plt.scatter(actuals, predictions, alpha=0.7)
        plt.xlabel("Actual G3")
        plt.ylabel("Predicted G3")
        plt.title("Actual vs Predicted (Sample 25)")
        st.pyplot(plt)

