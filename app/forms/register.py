from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError
from app.models.profesor import Profesor

class RegisterForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    curso = SelectField('Cursos', validators=[DataRequired()], choices=['Biologia', 'Física', 'Matemática', 'Inglés', 'Historia'])
    email = StringField('Correo', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    password2 = PasswordField('Repetir Contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrar')

    def validate_username(self, username):
        user = Profesor.query.filter_by(username=username.data).first()
        if user is not None:
            return ValidationError(f'El usuario {username.data} ya existe, intente con otro !')

    def validate_email(self, email):
        user = Profesor.query.filter_by(email=email.data).first()
        if user is not None:
            return ValidationError(f'El correo {email.data} ya existe, intente con otro !')
