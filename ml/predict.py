import pickle

# Load trained model
with open("ml/house_rent_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_rent(data):
    prediction = model.predict([data])
    return round(prediction[0], 2)