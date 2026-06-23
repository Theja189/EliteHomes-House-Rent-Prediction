from backend.models import Prediction
from backend.database import db
from flask import Blueprint, render_template, request
import pickle
import pandas as pd
import os

prediction_bp = Blueprint(
    "prediction",
    __name__
)

# =========================
# LOAD MODEL & ENCODERS
# =========================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "ml",
    "house_rent_model.pkl"
)

ENCODER_PATH = os.path.join(
    BASE_DIR,
    "ml",
    "encoders.pkl"
)

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(ENCODER_PATH, "rb") as f:
    encoders = pickle.load(f)

# =========================
# PREDICTION ROUTE
# =========================

@prediction_bp.route("/predict", methods=["GET", "POST"])
def predict():

    prediction = None

    if request.method == "POST":

        data = {
            "Building Type": request.form["building_type"],
            "Year Built": int(request.form.get("year_built", 0)),
            "BHK": int(request.form.get("bhk", 0)),
            "Size": int(request.form.get("size", 0)),
            "Floor": request.form["floor"],
            "Area Type": request.form["area_type"],
            "Area Locality": request.form["area_locality"],
            "City": request.form["city"],
            "Furnishing Status": request.form["furnishing_status"],
            "Tenant Preferred": request.form["tenant_preferred"],
            "Bathroom": int(request.form.get("bathroom", 0)),
            "Point of Contact": request.form["point_of_contact"]
        }
        
        print(data)
        df = pd.DataFrame([data])

        for col in encoders:
            df[col] = encoders[col].transform(df[col])

        prediction = "{:,}".format(
            round(model.predict(df)[0])
        )

        new_prediction = Prediction(
            city=request.form["city"],
            bhk=int(request.form["bhk"]),
            size=int(request.form["size"]),
            predicted_rent=prediction
        )

        db.session.add(new_prediction)
        db.session.commit()

    return render_template(
        "customer/predict.html",
        prediction=prediction
    )

@prediction_bp.route("/prediction-history")
def prediction_history():

    predictions = Prediction.query.all()

    return render_template(
        "customer/prediction-history.html",
        predictions=predictions
    )