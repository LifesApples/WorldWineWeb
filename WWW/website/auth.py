from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

import psycopg2

try:
    conn = psycopg2.connect(host = 'pgserver.mau.se',
                database = 'am4404',
                user = 'am4404',
                password = 'zxd0hy59')
    
except Exception as error:
    print(error)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    print("Tried logging in")
    if request.method == 'POST':
        username = request.form.get("form2Example11")
        print("Name was: " + str(username))
        username = request.form.get("Password")
        

    return render_template("login.html")

@auth.route("/logout")
def loginout():
    return "<p>Loginout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    print("Tried registering")
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

        try:
                cur = conn.cursor()

                insert_script = 'SET search_path = "WorldWineWeb", am4404, public; INSERT INTO users(username, password, email) VALUES (%s, %s, %s)'
                data = (username,email,password1)
                cur.execute(insert_script,data)
                conn.commit()
               
        except Exception as error:
            print(error)
            
        finally:
            if cur is not None:
                cur.close()
            if cur is not None:
                conn.close()
    return render_template("sign_up.html")
