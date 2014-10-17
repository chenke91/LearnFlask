from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import Length,Required,Email,EqualTo,Regexp
from wtforms import ValidationError
from ..models import User

class LoginForm(Form):
    email = StringField('Email', validators = [Required(),Length(1,64),Email()])
    password = PasswordField('password',validators = [Required()])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('Log in')
    
class RegistrationForm(Form):
    email = StringField('Email',validators = [Required(),Length(1,64),
                                                Email()])
    username = StringField('Username',validators = [
        Required(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,
                                        'Usernames must have only letters,numbers,dots or underscores')])
    password = PasswordField('Password',validators = [
        Required(),EqualTo('password2',message = 'Password must be match')])
    password2 = PasswordField('Confirm Password',validators = [Required()])
    submit = SubmitField('Register')

    def validate_email(form,field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(form,field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('Username already in use.')
