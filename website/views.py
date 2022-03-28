from unicodedata import category
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_user, login_required, login_url, current_user, logout_user
from .import db
import json

from website.models import PhoneBook

views = Blueprint('views' , __name__)

@views.route('/home', methods=['GET' , 'POST'])
@login_required
def home(): 
    if request.method == 'POST':
        name = request.form.get('name')
        number = request.form.get('number')

        if len(name) < 1:
            flash("Name too short!", category='error')
        else:
            newNumber = PhoneBook(name=name, number=number, user_id=current_user.id) 
            db.session.add(newNumber)
            db.session.commit()

    return render_template("home.html", user=current_user) 

@views.route('/delete-number' , methods=["POST"])
def delete_number():

    name = json.loads(request.name)
    nameID = name['nameID']
    name = PhoneBook.query.get(nameID)
    
    if name:
        if name.user_id == current_user.id:
            db.session.delete(name)
            db.session.commit()

    return jsonify({})