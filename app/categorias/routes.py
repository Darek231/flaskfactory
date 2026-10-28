
from flask import Blueprint,render_template,request,redirect,url_for,flash
from app.app import db
from app.categorias.models import Categoria
from app.auth.seguridad import login_requerido

categorias=Blueprint('categorias',__name__,template_folder='templates')

@categorias.route('/')
@login_requerido
def lista():
    datos=Categoria.query.all()
    return render_template('categorias.html',datos=datos)

@categorias.route('/crear',methods=['GET','POST'])
def crear():
    if request.method=='POST':
        nombre=request.form['nombre'].strip()
        descripcion=request.form.get('descripcion','').strip()

        if Categoria.query.filter_by(nombre=nombre).first():
            flash('Esta categoría ya existe.')
            return redirect(url_for('categorias.crear'))

        c=Categoria(nombre=nombre,descripcion=descripcion or None)
        db.session.add(c)
        db.session.commit()
        flash('Categoría creada correctamente.')
        return redirect(url_for('categorias.lista'))

    return render_template('formulario_categoria.html',dato=None)

@categorias.route('/editar/<int:id>',methods=['GET','POST'])
def editar(id):
    c=Categoria.query.get_or_404(id)

    if request.method=='POST':
        nombre=request.form['nombre'].strip()
        descripcion=request.form.get('descripcion','').strip()
        existente=Categoria.query.filter_by(nombre=nombre).first()

        if existente and existente.id_categoria!=c.id_categoria:
            flash('Ya existe una categoría con ese nombre.')
            return redirect(url_for('categorias.editar',id=id))

        c.nombre=nombre
        c.descripcion=descripcion or None
        db.session.commit()
        flash('Categoría actualizada correctamente.')
        return redirect(url_for('categorias.lista'))

    return render_template('formulario_categoria.html',dato=c)

@categorias.route('/eliminar/<int:id>',methods=['POST'])
def eliminar(id):
    c=Categoria.query.get_or_404(id)

    if c.anuncios:
        flash('No puedes eliminar una categoría que tiene anuncios asociados.')
        return redirect(url_for('categorias.lista'))

    db.session.delete(c)
    db.session.commit()
    flash('Categoría eliminada correctamente.')
    return redirect(url_for('categorias.lista'))
