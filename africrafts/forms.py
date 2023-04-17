from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField, validators


class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.Length(min=8, max=25)
    ])
    confirm = PasswordField('Repeat Password', [validators.DataRequired()])


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])


class ArtisanForm(FlaskForm):
    first_name = StringField('First Name', [validators.Length(min=2, max=25), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=2, max=25), validators.DataRequired()])
    shop_name = StringField('Shop Name', [validators.Length(min=2, max=25), validators.DataRequired()])
    email = StringField('Email', [validators.Length(min=2, max=25), validators.DataRequired()])
    phone = StringField('Phone', [validators.Length(min=2, max=25), validators.DataRequired()])
    city = StringField('City', [validators.Length(min=2, max=25), validators.DataRequired()])
    country = StringField('Country', [validators.Length(min=2, max=25), validators.DataRequired()])
    address = StringField('Address', [validators.Length(min=2, max=25), validators.DataRequired()])

    