from flask import (
    Blueprint,
    render_template,
    request,
    redirect
)

from models import Property
from database import db

import os

property_bp = Blueprint(
    "property",
    __name__
)

# =========================
# ADD PROPERTY
# =========================

@property_bp.route("/add-property", methods=["GET", "POST"])
def add_property():

    if request.method == "POST":

        title = request.form.get("title")
        city = request.form.get("city")
        rent = request.form.get("rent")
        bhk = request.form.get("bhk")
        area = request.form.get("area")
        furnishing = request.form.get("furnishing")

        image_file = request.files.get("image")

        image_name = ""

        if image_file and image_file.filename != "":

            image_name = image_file.filename

            upload_folder = os.path.join(
                os.path.dirname(__file__),
                "../../frontend/static/uploads"
            )

            os.makedirs(
                upload_folder,
                exist_ok=True
            )

            image_file.save(
                os.path.join(
                    upload_folder,
                    image_name
                )
            )

        property_obj = Property(
            title=title,
            city=city,
            rent=rent,
            bhk=bhk,
            area=area,
            furnishing=furnishing,
            image=image_name
        )

        db.session.add(property_obj)
        db.session.commit()

        return redirect("/properties")

    return render_template(
        "owner/add-property.html"
    )


# =========================
# VIEW PROPERTIES
# =========================

@property_bp.route("/properties")
def properties():

    properties = Property.query.all()

    return render_template(
        "owner/listing.html",
        properties=properties
    )

# =========================
# PROPERTY DETAILS
# =========================

@property_bp.route("/property/<int:property_id>")
def property_details(property_id):

    property = Property.query.get_or_404(
        property_id
    )

    return render_template(
        "owner/property-details.html",
        property=property
    )