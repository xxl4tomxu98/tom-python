from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
class LoginForm(FlaskForm):
    employee_number = StringField('Employee number', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField('Login')


class LogoutForm(FlaskForm):
    submit = SubmitField('Logout')

class AssignTable(FlaskForm):
    employee_number = StringField('Employee number', [DataRequired()])
    table_number = StringField('Table number', [DataRequired()])
    submit = SubmitField('Add to table')
