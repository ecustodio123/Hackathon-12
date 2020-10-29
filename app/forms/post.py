from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField, Field
from wtforms.validators import DataRequired
from app.models.alumno import Alumno
from datetime import datetime
from wtforms.fields import html5 as h5fields
from wtforms.widgets import html5 as h5widgets


class PostForm(FlaskForm):
    if datetime.now().strftime("%A") == 'Monday' or datetime.now().strftime("%A") == 'Tuesday' or datetime.now().strftime("%A") == 'Wednesday' or datetime.now().strftime("%A") == 'Thursday' or datetime.now().strftime("%A") == 'Friday':
    # if datetime.now().strftime("%A") == 'Saturday' or datetime.now().strftime("%A") == 'Sunday':
        alumno = SelectField('Alumno', validators=[DataRequired()], choices=['Kikito', 'Eduardo'])
        asistencia = SelectField('Asistencia', validators=[DataRequired()], choices=['Presente', 'Tardanza', 'No asistio'])
        tipoexamen = SelectField('Tipo de examen', validators=[DataRequired()], choices=['Oral', 'Escrito', 'Virtual'])
        post = h5fields.IntegerField('Nota', widget=h5widgets.NumberInput(min=0, max=20))
        # post = IntegerField('Nota', validators=[DataRequired()])
        SubmitField = SubmitField('Subir Nota')
    else:
        pass
        