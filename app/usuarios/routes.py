
from flask import Blueprint,render_template,request,redirect,url_for,flash
from app.app import db
from app.usuarios.models import Usuario

usuarios=Blueprint('usuarios',__name__,template_folder='templates')

@usuarios.route('/')
def lista():
    datos=Usuario.query.all()
    return render_template('usuarios.html',datos=datos)

@usuarios.route('/crear',methods=['GET','POST'])
def crear():
    if request.method=='POST':
        nombre=request.form['nombre'].strip()
        apellido=request.form['apellido'].strip()
        email=request.form['email'].strip()
        password=request.form['password']
        rol=request.form.get('rol','usuario')

        if Usuario.query.filter_by(email=email).first():
            flash('Ese correo ya está registrado.')
            return redirect(url_for('usuarios.crear'))

        u=Usuario(
            nombre=nombre,
            apellido=apellido,
            email=email,
            password=password,
            rol=rol
        )
        db.session.add(u)
        db.session.commit()
        flash('Usuario creado correctamente.')
        return redirect(url_for('usuarios.lista'))

    return render_template('formulario_usuario.html',dato=None)

@usuarios.route('/editar/<int:id>',methods=['GET','POST'])
def editar(id):
    u=Usuario.query.get_or_404(id)

    if request.method=='POST':
        nombre=request.form['nombre'].strip()
        apellido=request.form['apellido'].strip()
        email=request.form['email'].strip()
        existente=Usuario.query.filter_by(email=email).first()

        if existente and existente.id_usuario!=u.id_usuario:
            flash('Ese correo ya está registrado.')
            return redirect(url_for('usuarios.editar',id=id))

        u.nombre=nombre
        u.apellido=apellido
        u.email=email
        u.rol=request.form.get('rol','usuario')

        password=request.form.get('password','')
        if password:
            u.password=password

        db.session.commit()
        flash('Usuario actualizado correctamente.')
        return redirect(url_for('usuarios.lista'))

    return render_template('formulario_usuario.html',dato=u)

@usuarios.route('/eliminar/<int:id>',methods=['POST'])
def eliminar(id):
    u=Usuario.query.get_or_404(id)
    db.session.delete(u)
    db.session.commit()
    flash('Usuario eliminado correctamente.')
    return redirect(url_for('usuarios.lista'))
