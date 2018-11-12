#Flask dependencies
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

#App dependencies
from app.models import User


class LoginForm(FlaskForm):
    """
    class to manage Login Form.
    """
    identifier = StringField('Username or Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    """
    class to manage User registration form.
    """
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password',
        validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Register')

    def validate_username(self, username):
        """
        Method to validate if username already do not exist.
        """
        if User.query.filter_by(username=username.data).first() is not None:
            raise ValidationError('Please use a different username.')
        elif ' ' in username:
            raise ValidationError('Blanck spaces not allowed in username')

    def validate_email(self, email):
        """
        Method to validate if email already do not exist.
        """
        if User.query.filter_by(email=email.data).first() is not None:
            raise ValidationError('Please use a different email address.')
