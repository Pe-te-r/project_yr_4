from flask import Blueprint,render_template,redirect,url_for,flash
from .form import RegistrationForm,LoginForm
from my_app.models import User



auth_bp = Blueprint('auth_bp',__name__,template_folder='templates',static_folder='static')

@auth_bp.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_data={
            'first_name':form.first_name.data,
            'last_name':form.last_name.data,
            'email':form.email.data,
            'password':form.password.data,
        }
        user = User.add_user(**user_data)
        if not user:
            pass
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('auth_bp.login'))
    return  render_template('register.html',title='register',form=form)

        
@auth_bp.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user_data = {
            'email':form.email.data,
            'password':form.password.data
        }
        
        user = User.by_email(form.data.email)
        if not user:
            flash('User with this email not found.', 'error')
            return redirect(url_for('auth_bp.login'))
        if not user.verify_password(form.password.data):
            flash('User password not correct.', 'error')
            return redirect(url_for('auth_bp.login'))
        flash('Login was successful.', 'success')
        return redirect(url_for('login.html'),title='Login',form=form)

