# src/predict.py
import joblib

def predict_flight_price(duration, days_left):
    model = joblib.load('models/flight_price_model.pkl')
    price = model.predict([[duration, days_left]])
    print(f"Predicted flight price: ₹{price[0]:.2f}")
    return price[0]

if __name__ == "__main__":
    predict_flight_price(12, 25)