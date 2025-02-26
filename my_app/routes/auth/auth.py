from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from .form import RegistrationForm, LoginForm
from my_app.models import User

auth_bp = Blueprint("auth", __name__, template_folder="templates")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_data = {
            "full_name": form.full_name.data,
            "id_type": form.id_type.data,
            "national_id": form.id_number.data,
            "phone": form.phone_number.data,
            "email": form.email.data,
            "password": form.password.data,
        }
        user_exits = User.by_national_id(form.id_number.data)
        if user_exits:
            flash("User with the national ID already exists.", "danger")
        else:
            user = User.add_user(user_data)
            if user:
                flash("Your account has been created! You can now log in.", "success")
                return redirect(url_for("auth.login"))
            else:
                flash("An error occurred. Please try again.", "danger")
    else:
        print(form.errors)  # Print form errors for debugging
    return render_template("register.html", title="Register", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.by_national_id(form.id_number.data)
        if user and user.verify_password(form.password.data):
            login_user(user)
            flash("Login was successful.", "success")
            return redirect(url_for("home.home"))
        else:
            print("here")
            flash("Invalid national ID or password.", "danger")
    return render_template("login.html", title="Login", form=form)


@auth_bp.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("auth.login"))
