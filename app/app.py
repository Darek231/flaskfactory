
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db=SQLAlchemy()
migrate=Migrate()

def create_app():
    app=Flask(__name__,template_folder='templates',instance_relative_config=True)

    os.makedirs(app.instance_path,exist_ok=True)

    app.config['SECRET_KEY']='clave_secreta'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///bd_anuncios.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    db.init_app(app)
    migrate.init_app(app,db)

    from app.core.routes import core
    from app.auth.routes import auth
    from app.usuarios.routes import usuarios
    from app.categorias.routes import categorias
    from app.anuncios.routes import anuncios

    app.register_blueprint(core)
    app.register_blueprint(auth,url_prefix='/auth')
    app.register_blueprint(usuarios,url_prefix='/usuarios')
    app.register_blueprint(categorias,url_prefix='/categorias')
    app.register_blueprint(anuncios,url_prefix='/anuncios')

    from app.usuarios.models import Usuario
    from app.categorias.models import Categoria
    from app.anuncios.models import Anuncio

    return app
