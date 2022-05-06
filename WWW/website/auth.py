from unicodedata import name
from flask import Blueprint, render_template, request, flash
from db_connection import *

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        print("Name was: " + username)
        password = request.form.get("password1")
        print("Password was: " + password)
        
        
        try:
            
            insert_script = 'SET search_path = "WorldWineWeb", am4404, public; Select * from users where username = %s and "password"= %s'
            data = (username,password)
            print("Testing: " + insert_script)
            cur.execute(insert_script,data)
            print("The number of parts: ", cur.rowcount)
            conn.commit()

            if cur.rowcount < 1:
                flash("Wrong username or password", category="error")
            else:
                flash("Login sucessful!", category="success")
            
           
            
         

        except Exception as error:
            print(error)
                
     
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
