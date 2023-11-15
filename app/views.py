from flask import Blueprint
from flask import render_template, request

from .user import User
from datetime import datetime
from .db_handling import DB

views = Blueprint('views', __name__)

@views.route('/')
def home() -> str:
    return render_template("home.html")

@views.route('/login', methods=['GET', 'POST'])
def login() -> str:
    """
    Logs into DB, return an HTML template.
    """
    if request.method == 'POST':   
        user_data = DB.get_user(request.form['user_name'], request.form['password'])
        print(f'From database! {user_data}')
        return render_template("user_page.html", boolean=True, form_data=user_data, msg='Loged in successfully!')
    
    if request.method == 'GET':
        return render_template("login.html", bolean=True)

@views.route('/register', methods=['GET', 'POST'])
def register() -> str: 
    """
    Regiters a new user into DB, return an HTML template.
    """
    if request.method == 'POST': 
        registration = datetime.now().strftime("%Y-%m-%d %H:%M")
        user = User(request.form['user_name'], request.form['password'], registration)
        DB.add_user(user)
        
        return render_template("user_page.html", boolean=True, msg='Registered successfully!', form_data={
            user.name: [user.password, user.registration]
        })
    
    if request.method == 'GET':
        return render_template("register.html", bolean=True)

@views.route('/user', methods=['POST'])
def show_user() -> str:
    """
    returns an HTML template with some user data. (Vulnerable to SQL injection.)
    """
    if request.method == 'POST':        
        user_data = DB.get_user(request.form['user_name'], request.form['password'])
        return render_template("user_page.html", boolean=True, form_data=user_data)
    
    # Get method returns into home.html
    return render_template("home.html")