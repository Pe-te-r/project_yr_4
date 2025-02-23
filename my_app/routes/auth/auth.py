from flask import Blueprint,render_template,redirect,url_for
from form import RegistrationForm
from my_app.models import User
from my_app.routes.auth import auth_bp

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
        user = User(user_data)
        if not user:
            pass
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('auth_bp.login'))
    return  render_template('auth/register.html',title='register',form=form)

        