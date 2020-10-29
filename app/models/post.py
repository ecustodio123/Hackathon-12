from app import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alumno = db.Column(db.String(70), index=True)
    asistencia = db.Column(db.String(70), index=True)
    tipo_examen = db.Column(db.String(70), index=True)
    nota = db.Column(db.Integer, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.now())
    alumno_id = db.Column(db.Integer, db.ForeignKey('profesor.id'))

    def __repr__(self):
        return f'POST -> {self.nota}'