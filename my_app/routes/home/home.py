from flask import Blueprint,render_template,redirect,url_for,flash
from flask_login import login_required,current_user
from my_app.models import User



home_bp = Blueprint('home', __name__, template_folder='templates')

@home_bp.route('/home',methods=['GET'])
@home_bp.route('/',methods=['GET'])
# @login_required
def home():
    print(current_user)
    return render_template('home.html')
