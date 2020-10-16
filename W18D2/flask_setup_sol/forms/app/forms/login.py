from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()]) # we give this field a validator to make sure it is not left blank
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")

# All forms will be an instance of a class inheriting from FlaskForm
# We using properties imported from wtforms for the input fields
