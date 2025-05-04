DEMO Link:[Click here:](https://student-performance-app-kwappvkna3tbkhpeqvemypp.streamlit.app/)
## 📘 Student Performance Predictor App

This Streamlit app predicts students' final grades (G3) based on demographic and academic data using a linear regression model trained on the UCI "student-mat.csv" dataset.

### 🔧 Features

* **Single Input**: Enter values manually to get a single prediction.
* **Bulk Input**: Upload a CSV to get multiple predictions.
* **Visualization**: Visual comparison of actual vs. predicted grades.

### 📂 Files in Repository

* `app.py`: Main Streamlit app with UI.
* `student_model.pkl`: Trained linear regression model.
* `student-mat.csv`: Original dataset.
* `prediction.csv`: Sample dataset with 25 rows.
* `requirements.txt`: Dependencies for running the app.

### ✅ Technologies Used

* Python, Pandas, Scikit-learn, Streamlit, Matplotlib

### 📦 Setup Instructions

```bash
# Clone the repo and move into it
git clone https://github.com/your-username/student-performance-app.git
cd student-performance-app

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### ☁️ Deployment

* Use **Streamlit Cloud** or **Hugging Face Spaces** for fast deployment.

### 📈 Sample Inputs (Features)

* All 32 preprocessed numerical features after encoding from `student-mat.csv`

### 📧 Contact

Created by Vineet Kumar Saini. For queries, connect via LinkedIn or GitHub.

---

### 📄 requirements.txt

```text
pandas
numpy
scikit-learn
streamlit
matplotlib
```


