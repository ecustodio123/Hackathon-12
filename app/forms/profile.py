from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ProfileForm(FlaskForm):
    
    nombre = StringField('Nombre', validators=[DataRequired()])
    about_me = TextAreaField('Acerca de mi', validators=[DataRequired(), Length(min=0, max=180)])
    submit = SubmitField('Actualizar')