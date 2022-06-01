import this
from unittest import result
from flask import Blueprint, redirect, render_template, request, flash, url_for
from db_connection import *

# Länkar comments.py med main.py.
comments = Blueprint('comments', __name__)


@comments.route('/products', methods=['GET', 'POST'])
def addcomment():
    """försöker lägga till comment i databas"""
    print("skitpadig")
    if request.method == 'GET':
        print("hej jag kör")
        comment = request.args.get("comment")
        rating = request.args.get("rating")
        test = request.args.get("productid")
        print ("test: ",test)
        try:
            cur = conn.cursor()
            insert_script = "SET search_path = 'WorldWineWeb', am4404, public; select searchProduct('%s')" % (search_product)
            insert_script = "SET search_path = 'WorldWineWeb', am4404, public; select createcomment('%s','%s','%s','%s','%s')" % (comment, "username",)
            query = "SET search_path = 'WorldWineWeb', am4404, public; select updateurl('%s','%s');" % (orgValue,urlToSend)
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

    elif request.method == 'POST':
        print("hej jag e på dass")
        comment = request.form.get("comment")
        rating = request.form.get("rating")
        test = request.args.get("productid")
        
        

        try:
            cur = conn.cursor()

            insert_script = 'SET search_path = "WorldWineWeb", am4404, public; INSERT INTO commentsection(commenttext, commentrating,) VALUES (%s, %s,)'
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
        return render_template("product_page.html")