from flask import Blueprint, render_template, request, flash


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@auth.route("/logout")
def loginout():
    return "<p>Loginout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        #krav på användaren input med hjälp av en if-sats.
        if len(username) < 4:
            flash("Username must be greater than 4 characters", category="error")
        elif len(email) < 8:
            flash("Email must be greater than 8 characters", category="error")
        elif password1 != password2:
            flash("Passwords dont match", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters.", category="error")
        else: 
            flash("Account created!", category="success")

    return render_template("sign_up.html")
