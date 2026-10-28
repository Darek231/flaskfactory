
from app.app import db

class Categoria(db.Model):
    __tablename__ = 'categorias'

    id_categoria = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    descripcion = db.Column(db.Text, nullable=True)

    anuncios = db.relationship(
        'Anuncio',
        back_populates='categoria',
        lazy=True
    )

    def __repr__(self):
        return f'<Categoria {self.nombre}>'
