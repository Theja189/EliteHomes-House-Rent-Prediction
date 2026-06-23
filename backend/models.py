from database import db

# =========================

# USER MODEL

# =========================

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    role = db.Column(db.String(20), nullable=False, default="customer")


# =========================

# PROPERTY MODEL

# =========================

class Property(db.Model):
    
    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    city = db.Column(db.String(100), nullable=False)

    rent = db.Column(db.Float, nullable=False)

    bhk = db.Column(db.Integer, nullable=False)

    area = db.Column(db.Float, nullable=False)

    furnishing = db.Column(db.String(50), nullable=False)

    image = db.Column(db.String(255))


# =========================

# REVIEW MODEL

# =========================

class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), nullable=False)

    comment = db.Column(db.Text, nullable=False)

    rating = db.Column(db.Integer, nullable=False)

# =========================

# PREDICTION MODEL

# =========================

class Prediction(db.Model):
    __tablename__ = "predictions"

    id = db.Column(db.Integer, primary_key=True)

    city = db.Column(db.String(100))
    bhk = db.Column(db.Integer)
    size = db.Column(db.Integer)

    predicted_rent = db.Column(db.Integer)
    
# =========================

# BOOKING MODEL

# =========================

class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)

    customer_name = db.Column(db.String(100), nullable=False)

    property_name = db.Column(db.String(200), nullable=False)

    contact = db.Column(db.String(20), nullable=False)

