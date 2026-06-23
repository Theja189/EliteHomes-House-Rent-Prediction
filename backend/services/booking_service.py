from models import Booking
from database import db


def create_booking(
    customer_name,
    property_name,
    contact
):

    booking = Booking(
        customer_name=customer_name,
        property_name=property_name,
        contact=contact
    )

    db.session.add(booking)
    db.session.commit()

    return booking


def get_all_bookings():

    return Booking.query.all()


def get_booking_by_id(id):

    return Booking.query.get(id)