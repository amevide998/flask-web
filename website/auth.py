from flask import Blueprint

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return "<h1> login page </h1>"

@auth.route('/logout')
def logout():
    return "<h1> logout page </h1>"

@auth.route('signup')
def signup():
    return "<h1> signup page </h1>"