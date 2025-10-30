# ✈️ Flight Price Prediction

This project predicts flight ticket prices based on factors like airline, departure time, duration, stops, and days left before departure.  
It uses **Machine Learning (Linear Regression)** for building a predictive model.

---

## 📂 Project Structure

flight_price_prediction/
│
├── models/
│ └── flight_price_model.pkl
│
├── src/
│ ├── data_preprocessing.py
│ ├── model_training.py
│ ├── predict.py
│
├── airlines_flights_data.csv
├── EDA and model.ipynb
├── requirements.txt
└── README.md

## 🧩 Steps Involved  
1. **Data Preprocessing**  
   - Handle missing values  
   - Encode categorical variables  
   - Feature selection (`duration`, `days_left`)  

2. **Model Training**  
   - Trained using Linear Regression  
   - Evaluated with MAE, MSE, and R² metrics  

3. **Prediction**  
   - Saved model as `flight_price_model.pkl`  
   - Used `predict.py` to make new predictions  
