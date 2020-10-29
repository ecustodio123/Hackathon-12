from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5
from flask_login import UserMixin

class Alumno(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(70), index=True, unique=True)
    salon = db.Column(db.String(70), index=True)
    nota = db.Column(db.Integer, index=True)
    email = db.Column(db.String(140), index=True, unique=True)
    password = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.now())
    # posts = db.relationship('Post', backref="author", lazy="dynamic")

    def __repr__(self):
        return f'Alumno -> {self.nombre}'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def avatar(self, size):
        encoded = md5(self.email.lower().encode('UTF-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{encoded}?d=id_alumnoenticon&s={size}'

@login.user_loader
def load_user(id_alumno):
    return Alumno.query.get(int(id_alumno))        