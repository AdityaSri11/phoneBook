from unicodedata import category
from flask import Blueprint, render_template, request, flash, jsonify
from flask import after_this_request
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

@views.route('/delete-note', methods=['POST'])
def delete_note():

    note = json.loads(request.data)
    noteId = note['noteId']
    note = PhoneBook.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
                
    return jsonify({})

@views.route('/homepage',  methods=['GET' , 'POST'])
def about():
    return render_template("about.html", user=current_user) 
