from flask import Flask, render_template

from config import Config
from database import db
from models import *

from routes.auth_routes import auth_bp
from routes.property_routes import property_bp
from routes.booking_routes import booking_bp
from routes.dashboard_routes import dashboard_bp
from routes.review_routes import review_bp
from routes.prediction_routes import prediction_bp


app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

# =========================
# REGISTER BLUEPRINTS
# =========================

app.register_blueprint(auth_bp)

# =========================
# PROPERTY BLUEPRINTS
# =========================

app.register_blueprint(property_bp)

# =========================
# BOOKING BLUEPRINTS
# =========================

app.register_blueprint(booking_bp)

# =========================
# DASHBOARD BLUEPRINTS
# =========================

app.register_blueprint(dashboard_bp)

# =========================
# REVIEW BLUEPRINTS
# =========================

app.register_blueprint(review_bp)

# =========================
# PREDICTION BLUEPRINTS
# =========================

app.register_blueprint(prediction_bp)

# =========================
# HOME PAGE
# =========================

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)