
from flask import Blueprint,render_template,request,redirect,url_for,flash,session
from werkzeug.security import check_password_hash,generate_password_hash
from app.app import db
from app.usuarios.models import Usuario

auth=Blueprint('auth',__name__,template_folder='templates')

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form['email'].strip()
        password=request.form['password']
        u=Usuario.query.filter_by(email=email).first()

        if u:
            try:
                correcto=check_password_hash(u.password,password)
            except (ValueError,TypeError):
                correcto=False

            if not correcto and u.password==password:
                correcto=True

            if correcto:
                if u.password==password:
                    u.password=generate_password_hash(password)
                    db.session.commit()

                session['id_usuario']=u.id_usuario
                session['nombre']=u.nombre
                return redirect(url_for('core.inicio'))

        flash('Correo o contraseña incorrectos.')

    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('core.inicio'))
