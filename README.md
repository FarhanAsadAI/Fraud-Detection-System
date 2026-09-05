🛡️ Fraud Detection System

An end-to-end Machine Learning system for detecting potentially fraudulent transactions using Random Forest, SMOTE, FastAPI, and Streamlit.

The system provides a complete pipeline from transaction input to real-time fraud prediction and risk probability.

---

🚀 Live Demo

🖥️ Streamlit Dashboard

"Open Fraud Detection Dashboard" (https://fraud-detection-dashboard-whpgybsxlpmbij9r3vqfqk.streamlit.app/)

⚡ FastAPI

"Open Live API" (https://fraud-detection-api-29f55a6c.fastapicloud.dev/)

📚 API Documentation

"Open Swagger Documentation" (https://fraud-detection-api-29f55a6c.fastapicloud.dev/docs)

---

🎯 Project Overview

Fraudulent transactions can cause significant financial losses for businesses and customers. This project uses Machine Learning to analyze transaction characteristics and classify transactions as:

- ✅ Legitimate / Not Fraud
- 🚨 Potentially Fraudulent

The system also provides a risk probability to help understand the level of fraud risk associated with a transaction.

---

✨ Key Features

- 🤖 Machine Learning-based fraud detection
- 🌲 Random Forest classification
- ⚖️ SMOTE for handling class imbalance
- ⚡ Real-time prediction through FastAPI
- 🖥️ Interactive Streamlit dashboard
- 📊 Fraud risk probability
- 🔐 Transaction security feature analysis
- 🕒 Transaction time analysis
- 🌐 Deployed API
- 🚀 Live web dashboard

---

🏗️ System Architecture

                    User
                     │
                     ▼
          ┌─────────────────────┐
          │ Streamlit Dashboard │
          └──────────┬──────────┘
                     │
                     │ HTTP Request
                     ▼
          ┌─────────────────────┐
          │     FastAPI API     │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │ Data Preprocessing  │
          │     Pipeline        │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │   Random Forest     │
          │     Classifier      │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │ Fraud Prediction +  │
          │  Risk Probability   │
          └─────────────────────┘

---

🤖 Machine Learning

The project uses a Random Forest Classifier for fraud detection.

Because fraud datasets are often highly imbalanced, SMOTE (Synthetic Minority Over-sampling Technique) was used to improve the representation of fraudulent transactions during model training.

Model Pipeline

Raw Transaction Data
        ↓
Data Preprocessing
        ↓
Categorical Feature Encoding
        ↓
SMOTE
        ↓
Random Forest Classifier
        ↓
Fraud Prediction

---

📊 Model Performance

The trained model achieved approximately:

Metric| Score
Accuracy| ~98%
Precision| ~89%
Recall| ~55%
F1-Score| ~56%

Important Note

Fraud detection is an imbalanced classification problem. Therefore, recall is particularly important, because failing to identify an actual fraudulent transaction can be more costly than incorrectly flagging a legitimate transaction.

---

💳 Transaction Features

The system analyzes multiple transaction characteristics, including:

- Transaction amount
- Account age
- Total user transactions
- User average transaction amount
- Shipping distance
- Country
- BIN country
- Transaction channel
- Merchant category
- Promotional usage
- AVS match
- CVV result
- 3D Secure status
- Transaction hour
- Day of week
- Transaction month
- Weekend indicator

---

⚡ FastAPI Backend

The Machine Learning model is exposed through a FastAPI REST API.

The API receives transaction information in JSON format and returns the prediction and risk probability.

Example Response

{
    "prediction": 0,
    "risk_probability": 0.12
}

Where:

- "prediction = 0" → Not Fraud
- "prediction = 1" → Fraud

The API is deployed and available online.

---

🖥️ Streamlit Dashboard

The Streamlit dashboard provides a user-friendly interface where users can enter transaction information and analyze its fraud risk.

The dashboard:

1. Collects transaction information.
2. Sends the data to the FastAPI backend.
3. Receives the Machine Learning prediction.
4. Displays the fraud classification.
5. Displays the risk probability.
6. Shows a transaction summary.

---

🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Imbalanced-learn
- Random Forest
- SMOTE
- FastAPI
- Pydantic
- Streamlit
- Requests
- Joblib
- GitHub
- FastAPI Cloud

---

📁 Project Structure

Fraud-Detection-System/
│
├── README.md
│
├── api/
│   ├── main.py
│   └── requirements.txt
│
└── dashboard/
    ├── app.py
    └── requirements.txt

---

▶️ Run the API Locally

Navigate to the API directory:

cd api

Install the required dependencies:

pip install -r requirements.txt

Run the FastAPI application:

uvicorn main:app --reload

The API will be available locally through the FastAPI server.

---

▶️ Run the Dashboard Locally

Navigate to the dashboard directory:

cd dashboard

Install the required dependencies:

pip install -r requirements.txt

Run Streamlit:

streamlit run app.py

The dashboard will open in your browser.

---

🌐 Deployment

The project contains two deployed components:

Backend

FastAPI API deployed through FastAPI Cloud.

Frontend

Streamlit dashboard deployed through Streamlit Community Cloud.

The Streamlit dashboard communicates with the deployed FastAPI backend to perform real-time predictions.

---

🎓 Project Objective

The main objective of this project is to demonstrate how Machine Learning can be integrated into a complete real-world application rather than being limited to model training inside a notebook.

The project covers:

Data → Machine Learning → API → Deployment → User Interface

---

Machine Learning & AI Project
