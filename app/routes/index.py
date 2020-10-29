from app import app, db
from flask import render_template, request, flash, redirect, url_for
from app.forms.login import LoginForm
from app.forms.loginalumno import LoginAlumnoForm
from app.forms.register import RegisterForm
from app.forms.registeralumno import RegisterAlumnoForm
from app.forms.post import PostForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models.alumno import Alumno
from app.models.profesor import Profesor
from app.models.post import Post
from werkzeug.urls import url_parse
from datetime import datetime

@app.route('/')
@app.route('/inicio')
def index():
    return render_template('index.html', title='Inicio')

@app.route('/inicio-alumno')
def indexalumno():
    return render_template('index_alumno.html', title='Inicio')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Profesor.query.filter_by(email=form.email.data).first()
        if user is None:
            flash(f'No se encuentra el correo del profesor')
            return redirect(url_for('login'))
        if not user.check_password(form.password.data):
            flash(f'La clave ingresada es erronea')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('views/login.html', title='Login', form=form)

@app.route('/loginalumno', methods=['GET', 'POST'])
def loginalumno():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginAlumnoForm()
    if form.validate_on_submit():
        user = Alumno.query.filter_by(email=form.email.data).first()
        if user is None:
            flash(f'No se encuentra el correo')
            return redirect(url_for('loginalumno'))
        if not user.check_password(form.password.data):
            flash(f'La clave ingresada es erronea')
            return redirect(url_for('loginalumno'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('indexalumno'))
    return render_template('views/login_alumno.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = Profesor(nombre=form.nombre.data, email=form.email.data, curso=form.curso.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Exito !, se registro como profesor')
        return redirect(url_for('login'))
    return render_template('views/register.html', title='Registro', form=form)

@app.route('/registeralumno', methods=['GET', 'POST'])
def registeralumno():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterAlumnoForm()
    if form.validate_on_submit():
        user = Alumno(nombre=form.nombre.data, email=form.email.data, salon=form.salon.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Exito !, se registro como alumno')
        return redirect(url_for('login'))
    return render_template('views/register-alumno.html', title='Registro', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/profile/<nombre>', methods=['GET', 'POST'])
@login_required
def profile(nombre):
    form = PostForm()
    if form.validate_on_submit():
        post = Post(alumno=form.alumno.data, asistencia=form.asistencia.data, tipo_examen=form.tipoexamen.data ,nota=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Se coloc la nota !')
        return redirect(url_for('profile', nombre=current_user.nombre))
    user = Profesor.query.filter_by(nombre=nombre).first_or_404()
    return render_template('views/profile.html', title=f'Perfil {nombre}', user=user, form=form)   

@app.route('/notas/<nombre>', methods=['GET', 'POST'])
@login_required
def notas(nombre):
    form = PostForm()
    if form.validate_on_submit():
        post = Post(nota=form.post.data)
        db.session.add(post)
        db.session.commit()
        flash('Se coloc la nota !')
        return redirect(url_for('notas', nombre=current_user.nombre))
    user = Alumno.query.filter_by(nombre=nombre).first_or_404()
    return render_template('views/profile.html', title=f'Perfil {nombre}', user=user, form=form)   

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now()
        db.session.commit()