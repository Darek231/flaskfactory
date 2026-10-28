
from app.app import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(20), nullable=False, default='usuario')
    fecha_registro = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    anuncios = db.relationship(
        'Anuncio',
        back_populates='usuario',
        lazy=True
    )

    def __repr__(self):
        return f'<Usuario {self.email}>'
