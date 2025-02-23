from flask import Blueprint
from form import RegistrationForm


auth_bp = Blueprint('auth_bp',__name__,template_folder='templates',static_folder='static')

@auth_bp.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():