# STEP 1 - Import required modules
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_pymongo import PyMongo
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

# import secrets
# secret_key = secrets.token_urlsafe(24)  # Generates a secure random string
# print(secret_key)


# STEP 2 - Create Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'G1hUvuLTwh3PcHskmFB6E_BEtzkTWCKN'  # Change this for security
app.config["MONGO_URI"] = "mongodb://mongo:27017/flask_database"

# STEP 3 - Set up MongoDB connection
mongo = PyMongo(app)
db = mongo.db
users = db.users  # Collection for user data
todos = db.todos  # Collection for to-do tasks

# STEP 4 - Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"  # Redirect to login page if not logged in

# User Loader Function
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

@login_manager.user_loader
def load_user(user_id):
    user_data = users.find_one({"_id": ObjectId(user_id)})
    if user_data:
        return User(str(user_data["_id"]))
    return None

# STEP 5 - Forms for Login & Registration
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# STEP 6 - Routes and Views
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = generate_password_hash(form.password.data)
        
        if users.find_one({"username": username}):
            flash("Username already exists. Please choose another.", "danger")
            return redirect(url_for("register"))
        
        users.insert_one({"username": username, "password": password})
        flash("Account created! Please login.", "success")
        return redirect(url_for("login"))

    return render_template("register.html", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = users.find_one({"username": form.username.data})
        if user and check_password_hash(user["password"], form.password.data):
            login_user(User(str(user["_id"])))
            flash("Login successful!", "success")
            return redirect(url_for("index"))
        flash("Invalid credentials. Try again.", "danger")
    
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))

@app.route("/", methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree, 'user_id': current_user.id})
        return redirect(url_for('index'))
    
    # Fetch only the logged-in user's tasks
    all_todos = todos.find({'user_id': current_user.id})
    return render_template('index.html', todos=all_todos)

@app.post("/<id>/delete/")
@login_required
def delete(id):
    todos.delete_one({"_id": ObjectId(id), "user_id": current_user.id})  # Ensuring only owner can delete
    return redirect(url_for('index'))

# STEP 7 - Run the Flask app
if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(host="0.0.0.0", port=5000, debug=True)
