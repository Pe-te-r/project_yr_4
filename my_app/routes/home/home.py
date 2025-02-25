from flask import Blueprint,render_template,redirect,url_for,flash

from my_app.models import User



home_bp = Blueprint('home', __name__, template_folder='templates')

@home_bp.route('/home',methods=['GET'])
@home_bp.route('/',methods=['GET'])
def home():
    return render_template('home.html')
