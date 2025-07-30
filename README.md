# 🏠 California Housing Price Predictor

A responsive and intuitive web application powered by machine learning that estimates **median house prices across California** using key demographic and geographic indicators.



## 🎯 Purpose of the Project

This project illustrates the use of machine learning for solving practical prediction tasks. Users can interact with the app by providing custom neighborhood parameters, and receive real-time home price predictions, accompanied by informative visualizations and map-based insights.



## 🌟 Highlights

-  **User-Friendly Interface** – Clean sliders and hints for easy data input  
-  **Instant Predictions** – Fast output using a trained Random Forest model  
-  **Map Integration** – Visualize locations using latitude and longitude  
-  **Smart Responses** – Emoji-based feedback for high/low price predictions  
-  **Streamlit-Powered** – Entire app built with Python and open-source tools



## 🧰 Technology Stack

| Component        | Technology               |
|------------------|---------------------------|
| Programming Lang | Python 3.12+              |
| Web Framework    | Streamlit                 |
| ML Library       | Scikit-learn              |
| Model Storage    | Joblib                    |
| Visualization    | Plotly                    |
| Mapping Tool     | `st.map()` (Streamlit)    |
| Styling          | HTML + CSS injection      |



## 📊 Dataset Details

- **Source**: `fetch_california_housing()` from `sklearn.datasets`
  
- **Attributes Used**:
  - `MedInc` – Median income in the block
  - `HouseAge` – Median age of houses
  - `AveRooms` – Average number of rooms per house
  - `AveBedrms` – Average number of bedrooms
  - `Population` – Total population in the block
  - `AveOccup` – Average occupancy per household
  - `Latitude`, `Longitude` – Geographic coordinates



## 🚀 Getting Started

 **Clone the repository**
   
   git clone https://github.com/your-username/california-housing-predictor.git
   cd california-housing-predictor
   
   **Install the required libraries**

   pip install -r requirements.txt
  
  **Launch the application**

   streamlit run app.py
   
**📁 Project Structure**

app.py	Main Streamlit app script

model.pkl	Pre-trained Random Forest model

train_model.py	Script to train and export the ML model

requirements.txt	List of required Python libraries

README.md	Project documentation and usage guide


# Screenshots 

<img width="1920" height="1080" alt="Screenshot (140)" src="https://github.com/user-attachments/assets/91513930-a292-44ad-86bb-758e0ecd82a6" />

<img width="1920" height="1080" alt="Screenshot (141)" src="https://github.com/user-attachments/assets/de66f0de-e7c8-4786-849b-72fe358087dd" />


