from flask import Flask
from psycopg2 import *

conn= None
cur = None


try:
    #koden nedan kopplar till databasen
    #se postgres properties för att hitta rätt nycklar
    import psycopg2
    conn = psycopg2.connect(
                host = 'pgserver.mau.se',
                database = 'am4404',
                user = 'am4404',
                password = 'zxd0hy59')

    cur = conn.cursor()
    

    #exekverar SQL queries
    #Syntax är samma som i SQL
    #'%s' är en placeholder för kommande variabler
    #sql kan utföras på två sätt, antinge med cur.execute eller create_script
    
    #cur.execute("CREATE TABLE pyexample (id int SERIAL PRIMARY KEY, name VARCHAR(50));")

    #cur.execute("INSERT INTO pyexample (name) VALUES(%s, %s)", ("Klaudia"))

    create_script = ''' CREATE TABLE IF NOT EXISTS pyexample(
                            id      int PRIMARY KEY,
                            name varchar(40) NOT NULL,
                            email varchar(40))'''
    cur.execute(create_script)

    insert_script = 'INSERT INTO pyexample (id, name, email) VALUES (%s, %s, %s,)'
    insert_value =(1, 'Klaudia')

    cur.execute(insert_script, insert_value)

    #detta sparar all SQL som man kör
    conn.commit()
    
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if cur is not None:
        conn.close()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'WWW'



    from .views import views
    from .auth import auth
    ##from .scraper import scraper

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
   ## app.register_blueprint(scraper, url_prefix='/')
  ##  imageScraper = scraper()
   ## imageScraper.searchPics("Three Hearts","Krönleins","Burk")
   

    return app



