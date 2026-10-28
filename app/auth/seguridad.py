
from functools import wraps
from flask import session,redirect,url_for,flash

def login_requerido(f):
    @wraps(f)
    def decorador(*args,**kwargs):
        if 'id_usuario' not in session:
            flash('Debes iniciar sesión para acceder.')
            return redirect(url_for('auth.login'))
        return f(*args,**kwargs)
    return decorador
