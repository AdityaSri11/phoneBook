from flask import Blueprint, render_template
from flask_login import login_user, login_required, login_url, current_user, logout_user

views = Blueprint('views' , __name__)

@views.route('/home')
@login_required
def home():
    return render_template("home.html", user=current_user)