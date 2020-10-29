from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError
from app.models.alumno import Alumno

class RegisterAlumnoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    salon = SelectField('Salones', validators=[DataRequired()], choices=['1°Primaria', '2°Primaria', '3°Primaria', '4°Primaria', '5°Primaria', '6°Primaria', '1°Secundaria', '2°Secundaria', '3°Secundaria', '4°Secundaria', '5°Secundaria'])
    email = StringField('Correo', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    password2 = PasswordField('Repetir Contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrar')

    def validate_username(self, nombre):
        user = Alumno.query.filter_by(nombre=nombre.data).first()
        if user is not None:
            return ValidationError(f'El usuario {nombre.data} ya existe, intente con otro !')

    def validate_email(self, email):
        user = Alumno.query.filter_by(email=email.data).first()
        if user is not None:
            return ValidationError(f'El correo {email.data} ya existe, intente con otro !')
