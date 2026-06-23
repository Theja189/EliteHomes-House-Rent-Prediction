from flask import (
    Blueprint,
    render_template,
    request,
    redirect
)

from models import Property
from services.booking_service import (
    create_booking,
    get_all_bookings
)

booking_bp = Blueprint(
    "booking",
    __name__
)

# =========================
# BOOK PROPERTY
# =========================

@booking_bp.route(
    "/book-property/<int:property_id>",
    methods=["GET", "POST"]
)
def book_property(property_id):

    property = Property.query.get_or_404(
        property_id
    )

    if request.method == "POST":

        customer_name = request.form.get(
            "customer_name"
        )

        contact = request.form.get(
            "contact"
        )

        create_booking(
            customer_name,
            property.title,
            contact
        )

        return redirect(
            "/dashboard"
        )

    return render_template(
        "customer/booking.html",
        property=property
    )


# =========================
# BOOKING HISTORY
# =========================

@booking_bp.route("/booking-history")
def booking_history():

    bookings = get_all_bookings()

    return render_template(
        "customer/booking-history.html",
        bookings=bookings
    )