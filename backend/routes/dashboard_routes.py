from flask import (
    Blueprint,
    render_template
)

from backend.models import (
    User,
    Property,
    Booking,
    Review,
    Prediction
)

dashboard_bp = Blueprint(
    "dashboard",
    __name__
)

@dashboard_bp.route("/dashboard")
def dashboard():

    total_users = User.query.count()

    total_properties = Property.query.count()

    total_bookings = Booking.query.count()

    total_reviews = Review.query.count()

    total_predictions = Prediction.query.count()

    recent_bookings = Booking.query.order_by(
        Booking.id.desc()
    ).limit(5).all()

    return render_template(
        "admin/dashboard.html",
        total_users=total_users,
        total_properties=total_properties,
        total_bookings=total_bookings,
        total_reviews=total_reviews,
        total_predictions=total_predictions,
        recent_bookings=recent_bookings
    )