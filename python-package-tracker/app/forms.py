from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, BooleanField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from map.map import map

values = map.keys()


class ShippingForm(FlaskForm):
    sender_name = StringField('Sender Name', validators=[DataRequired()])
    recipient_name = StringField('Recipient Name', validators=[DataRequired()])
    origin = SelectField("Origin", choices=values,
                         validators=[DataRequired()])
    destination = SelectField("Destination", choices=values,
                              validators=[DataRequired()])
    express_shipping = BooleanField("Express Shipping")
    submit = SubmitField("Submit")
    cancel = SubmitField("Cancel")


class LoginForm(FlaskForm):
    name = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class LogoutForm(FlaskForm):
    submit = SubmitField('Logout')
