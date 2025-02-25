from flask import Blueprint,render_template,redirect,url_for,flash
from .form import RegistrationForm,LoginForm
from my_app.models import User



auth_bp = Blueprint('auth', __name__, template_folder='templates')

@auth_bp.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_data={
            'full_name':form.full_name.data,
            'id_type':form.id_type.data,
            'national_id':form.id_number.data,
            'phone':form.phone_number.data,
            'email':form.email.data,
            'password':form.password.data,
        }

        user = User.add_user(user_data)
        print(user)
        if not user:
            flash('Your account has been created! You can now log in.', 'success')
            return render_template(url_for('auth.register'))
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('auth.login'))
    return  render_template('register.html',title='register',form=form)

        
@auth_bp.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        print(form.email.data)
        user_data = {
            'email':form.email.data,
            'password':form.password.data
        }
        
        user = User.by_email(form.email.data)
        if not user:
            flash('User with this email not found.', 'error')
            return redirect(url_for('auth.login'))
        if not user.verify_password(form.password.data):
            flash('User password not correct.', 'error')
            return redirect(url_for('auth.login'))
        flash('Login was successful.', 'success')
        return 'success'
    return render_template('login.html',title='Login',form=form)


@auth_bp.route('/logout',methods=['GET'])
def logout():
    pass