from flask import (
    Blueprint,
    render_template,
    request,
    redirect
)

from backend.models import Review
from backend.database import db

review_bp = Blueprint(
    "review",
    __name__
)

@review_bp.route("/reviews", methods=["GET", "POST"])
def reviews():

    if request.method == "POST":

        username = request.form.get("username")
        comment = request.form.get("comment")
        rating = request.form.get("rating")

        review = Review(
            username=username,
            comment=comment,
            rating=rating
        )

        db.session.add(review)
        db.session.commit()

        return redirect("/reviews")

    reviews = Review.query.all()

    return render_template(
        "customer/reviews.html",
        reviews=reviews
    )