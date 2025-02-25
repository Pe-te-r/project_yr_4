from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class RegistrationForm(FlaskForm):
    id_type = SelectField('ID Type', choices=[
        ('Kenyan Citizen', 'Kenyan Citizen'),
        ('Foreign Resident', 'Foreign Resident'),
        ('Refugee', 'Refugee'),
        ('Mandate Number', 'Mandate Number')
    ], validators=[DataRequired()])
    id_number = IntegerField('ID Number', validators=[DataRequired(), NumberRange(min=10000000, max=99999999)])
    full_name = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=50)])
    phone_number = IntegerField('Phone Number', validators=[DataRequired(), NumberRange(min=700000000, max=799999999)])
    submit = SubmitField('Proceed')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')