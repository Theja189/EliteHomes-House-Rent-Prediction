from models import User
from database import db


def create_user(name, email, password, role="customer"):

    user = User(
        name=name,
        email=email,
        password=password,
        role=role
    )

    db.session.add(user)
    db.session.commit()

    return user


def get_user_by_email(email):

    return User.query.filter_by(
        email=email
    ).first()