from app import app, db
from flask import render_template, request, flash, redirect, url_for
from app.forms.login import LoginForm
from app.forms.loginalumno import LoginAlumnoForm
from app.forms.register import RegisterForm
from app.forms.registeralumno import RegisterAlumnoForm
from app.forms.post import PostForm
from  import current_user, login_user, logout_user, login_required
from app.models.alumno import Alumno
from app.models.profesor import Profesor
from app.models.post import Post
from werkzeug.urls import url_parse
from datetime import datetime

@app.route('/')
@app.route('/inicio')
def indexalumno():
    return render_template('index_alumno.html', title='Inicio')
