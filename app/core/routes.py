
from flask import Blueprint,render_template

core=Blueprint('core',__name__)

@core.route('/')
def inicio():
    return render_template('index.html')
