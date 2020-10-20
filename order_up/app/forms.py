from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired
class LoginForm(FlaskForm):
    employee_number = StringField('Employee number', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField('Login')


class LogoutForm(FlaskForm):
    submit = SubmitField('Logout')

class AssignTable(FlaskForm):
    employees = SelectField('Servers', [DataRequired()])
    tables = SelectField('Tables', [DataRequired()])
    submit = SubmitField('assign employee to table')
