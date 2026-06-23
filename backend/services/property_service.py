from models import Property
from database import db


def create_property(
    title,
    city,
    rent,
    bhk,
    area,
    furnishing,
    image
):

    property_obj = Property(
        title=title,
        city=city,
        rent=rent,
        bhk=bhk,
        area=area,
        furnishing=furnishing,
        image=image
    )

    db.session.add(property_obj)
    db.session.commit()

    return property_obj


def get_all_properties():

    return Property.query.all()


def get_property_by_id(id):

    return Property.query.get(id)


def delete_property(id):

    property_obj = Property.query.get(id)

    if property_obj:

        db.session.delete(property_obj)
        db.session.commit()

    return property_obj