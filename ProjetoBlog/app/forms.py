from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

class Cadastro(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])
    enviar = SubmitField('enviar')