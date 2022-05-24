from unicodedata import name
from flask import Blueprint, render_template, request, flash
from db_connection import *


# Länkar comments.py med main.py.
comments = Blueprint('comments', __name__)


@comments.route('/comments', methods=['GET', 'POST'])
def addcoments():
    """försöker lägga till comment i databas"""
    if request.method == 'POST':
        comment = request.form.get("kommentar")
        rating = request.form.get("rating")

        try:
            cur = conn.cursor()

            insert_script = 'SET search_path = "WorldWineWeb", am4404, public; INSERT INTO addComment(comment, rating,) VALUES (%s, %s,)'
            data = (comment,rating)
            cur.execute(insert_script,data)
            conn.commit()
         
        except Exception as error:
            print(error)
            
        finally:
            if cur is not None:
                cur.close()
            if cur is not None:
                conn.close()
                
    return render_template("comments.html")