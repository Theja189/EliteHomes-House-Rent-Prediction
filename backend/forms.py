from flask_wtf import FlaskForm

from wtforms import (
StringField,
PasswordField,
SubmitField,
SelectField,
FloatField,
IntegerField
)

from wtforms.validators import (
DataRequired,
Email,
Length
)

# =========================

# REGISTER FORM

# =========================

class RegisterForm(FlaskForm):
    name = StringField(
    "Full Name",
    validators=[DataRequired(), Length(min=3, max=100)]
)

email = StringField(
    "Email",
    validators=[DataRequired(), Email()]
)

password = PasswordField(
    "Password",
    validators=[DataRequired(), Length(min=6)]
)

role = SelectField(
    "Role",
    choices=[
        ("customer", "Customer"),
        ("owner", "Owner"),
        ("admin", "Admin")
    ]
)

submit = SubmitField("Register")


# =========================

# LOGIN FORM

# =========================
 
class LoginForm(FlaskForm):
    
    email = StringField(
    "Email",
    validators=[DataRequired(), Email()]
)

password = PasswordField(
    "Password",
    validators=[DataRequired()]
)

submit = SubmitField("Login")

# =========================

# PROPERTY FORM

# =========================

class PropertyForm(FlaskForm):
    
    title = StringField(
    "Property Title",
    validators=[DataRequired()]
)

city = StringField(
    "City",
    validators=[DataRequired()]
)

rent = FloatField(
    "Rent",
    validators=[DataRequired()]
)

bhk = IntegerField(
    "BHK",
    validators=[DataRequired()]
)

area = FloatField(
    "Area",
    validators=[DataRequired()]
)

furnishing = SelectField(
    "Furnishing",
    choices=[
        ("Furnished", "Furnished"),
        ("Semi-Furnished", "Semi-Furnished"),
        ("Unfurnished", "Unfurnished")
    ]
)

submit = SubmitField("Save Property")

