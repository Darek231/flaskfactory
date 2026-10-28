
from flask import Blueprint,render_template,request,redirect,url_for,flash
from app.app import db
from app.anuncios.models import Anuncio
from app.categorias.models import Categoria
from app.usuarios.models import Usuario
from app.auth.seguridad import login_requerido

anuncios=Blueprint('anuncios',__name__,template_folder='templates')

@anuncios.route('/')
@login_requerido
def lista():
    datos=Anuncio.query.all()
    return render_template('anuncios.html',datos=datos)

@anuncios.route('/crear',methods=['GET','POST'])
def crear():
    categorias=Categoria.query.all()
    usuarios=Usuario.query.all()

    if request.method=='POST':
        a=Anuncio(
            titulo=request.form['titulo'],
            descripcion=request.form['descripcion'],
            id_usuario=int(request.form['id_usuario']),
            id_categoria=int(request.form['id_categoria'])
        )
        db.session.add(a)
        db.session.commit()
        flash('Anuncio creado correctamente.')
        return redirect(url_for('anuncios.lista'))

    return render_template('formulario_anuncio.html',dato=None,categorias=categorias,usuarios=usuarios)

@anuncios.route('/editar/<int:id>',methods=['GET','POST'])
def editar(id):
    a=Anuncio.query.get_or_404(id)
    categorias=Categoria.query.all()
    usuarios=Usuario.query.all()

    if request.method=='POST':
        a.titulo=request.form['titulo']
        a.descripcion=request.form['descripcion']
        a.id_usuario=int(request.form['id_usuario'])
        a.id_categoria=int(request.form['id_categoria'])
        db.session.commit()
        flash('Anuncio actualizado correctamente.')
        return redirect(url_for('anuncios.lista'))

    return render_template('formulario_anuncio.html',dato=a,categorias=categorias,usuarios=usuarios)

@anuncios.route('/eliminar/<int:id>',methods=['POST'])
def eliminar(id):
    a=Anuncio.query.get_or_404(id)
    db.session.delete(a)
    db.session.commit()
    flash('Anuncio eliminado correctamente.')
    return redirect(url_for('anuncios.lista'))
