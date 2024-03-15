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
    msg = None
    if request.method == "GET":
        user_name = request.args.get('user_name')
        password = request.args.get('password')
    elif request.method == "POST":
        user_name = request.form["user_name"]
        password = request.form["password"]
    user_data = DB.get_user(user_name, password)
    if user_data: 
        msg = "Logged in successfully" 
    else: 
        msg = "You are unable to log in, please register before logging in."
        
    if request.method == "GET" and not user_name and not password:
        return render_template("login.html")
    
    return render_template("user_page.html", boolean=True, form_data=user_data, msg=msg)

@views.route('/register', methods=['GET', 'POST'])
def register() -> str: 
    """
    Regiters a new user into DB, return an HTML template.
    """
    user_name, password = "", ""
    if request.method == "GET":
        user_name = request.args.get('user_name')
        password = request.args.get('password')
    elif request.method == "POST":
        user_name = request.form["user_name"]
        password = request.form["password"]
        
    registration = datetime.now().strftime("%Y-%m-%d %H:%M")
    user = User(user_name, password, registration)
    DB.add_user(user)
    
    if request.method == "GET" and not user_name and not password:
        return render_template("register.html")
    
    return render_template("user_page.html", boolean=True, msg='Registered successfully!', form_data={
        user.name: [user.password, user.registration]
    })
    
@views.route('/user', methods=['GET', 'POST'])
def show_user() -> str:
    """
    returns an HTML template with some user data. (Vulnerable to SQL injection.)
    """
    if request.method == 'POST':        
        user_data = DB.get_user(request.form['user_name'], request.form['password'])
        return render_template("user_page.html", boolean=True, form_data=user_data)
    
    # Get method returns into home.html
    return render_template("home.html")
