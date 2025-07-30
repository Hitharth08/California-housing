import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("model.pkl")

# Page config
st.set_page_config(page_title="CaliforniaHomeValue Explorer", layout="wide")

# White background and black text styling
st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff;
        color: #000000;
    }
    .stSidebar {
        background-color: #f5f5f5;
    }
    .title-style {
        font-size: 36px;
        font-weight: 800;
        color: #222222;
    }
    .predict-box {
        background-color: #f0f0f0;
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        margin-top: 20px;
    }
    .predict-box h1 {
        font-size: 36px;
        color: #111111;
    }
    .predict-box p {
        font-size: 18px;
        color: #333333;
    }
    .stButton>button {
        background-color: #ffffff !important;
        color: #000000 !important;
        font-weight: bold;
        border: 1px solid #000000;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-style">🏘️ CaliforniaHomeValue Explorer</div>', unsafe_allow_html=True)
st.write("Use ML to estimate median house values in California districts.")

# Sidebar Inputs
st.sidebar.header("📍 Input Details")

features = {
    "MedInc": "Median Income (in $10,000)",
    "HouseAge": "Median Age of Houses",
    "AveRooms": "Average Rooms",
    "AveBedrms": "Average Bedrooms",
    "Population": "Population",
    "AveOccup": "Avg. Household Size",
    "Latitude": "Latitude",
    "Longitude": "Longitude"
}

inputs = []
for key, label in features.items():
    value = st.sidebar.number_input(label, min_value=0.0, max_value=100.0, value=5.0, step=0.1)
    inputs.append(value)

# Prediction section
if st.button("🔎 Estimate Home Value"):
    arr = np.array(inputs).reshape(1, -1)
    prediction = model.predict(arr)[0] * 100000

    if prediction > 600000:
        msg = "🏆 Premium Location!"
        color = "#4CAF50"  # green
    elif prediction > 300000:
        msg = "💼 Great Value!"
        color = "#FFC107"  # amber
    else:
        msg = "💡 Affordable Area"
        color = "#F44336"  # red

    st.markdown(f"""
        <div class="predict-box" style="border-left: 8px solid {color};">
            <h1>${prediction:,.2f}</h1>
            <p>{msg}</p>
        </div>
    """, unsafe_allow_html=True)
import pandas as pd

# Extract Latitude and Longitude from inputs (based on order)
latitude = inputs[-2]
longitude = inputs[-1]

if latitude != 0.0 or longitude != 0.0:
    map_data = pd.DataFrame({'lat': [latitude], 'lon': [longitude]})
    st.write("📍 Approximate Property Location:")
    st.map(map_data)



