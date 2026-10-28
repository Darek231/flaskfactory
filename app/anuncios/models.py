
from app.app import db
from sqlalchemy import func

class Anuncio(db.Model):
    __tablename__ = 'anuncios'

    id_anuncio = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    fecha_publicacion = db.Column(
        db.DateTime,
        nullable=False,
        server_default=func.now()
    )

    id_usuario = db.Column(
        db.Integer,
        db.ForeignKey('usuarios.id_usuario'),
        nullable=False
    )

    id_categoria = db.Column(
        db.Integer,
        db.ForeignKey('categorias.id_categoria'),
        nullable=False
    )

    usuario = db.relationship(
        'Usuario',
        back_populates='anuncios'
    )

    categoria = db.relationship(
        'Categoria',
        back_populates='anuncios'
    )

    def __repr__(self):
        return f'<Anuncio {self.titulo}>'
