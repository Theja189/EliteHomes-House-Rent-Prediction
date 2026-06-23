from flask import Blueprint, render_template, request, redirect, url_for, flash

from services.auth_service import (
    create_user,
    get_user_by_email
)

auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = get_user_by_email(email)

        if existing_user:

            flash(
                "Email already exists",
                "danger"
            )

            return redirect(
                url_for("auth.register")
            )

        create_user(
            name,
            email,
            password
        )

        flash(
            "Registration Successful",
            "success"
        )

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "register.html"
    )


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = get_user_by_email(email)

        if user and user.password == password:

            flash(
                "Login Successful",
                "success"
            )

            return redirect(
                "/dashboard"
            )

        flash(
            "Invalid Email or Password",
            "danger"
        )

    return render_template(
        "login.html"
    )