import this
from flask import Blueprint, render_template
from db_connection import *

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/products')
def product():
    print("Products found!")
    cur = conn.cursor()
    insert_script = 'SET search_path = "WorldWineWeb", am4404, public; Select getproducts(10)'
    cur.execute(insert_script)
    records = cur.fetchone()
    liste = []
    liste = list(records)

    lista = str(liste).split(",")
    for i in lista:
        print(i)
        print()
      
    ##print("Returned: ", records)
    conn.commit()
    return render_template("products.html")

"""

cur = conn.cursor()
insert_script = 'SET search_path = "WorldWineWeb", am4404, public; Select getallproducts()'
cur.execute(insert_script)
print("Returned products: " + cur.rowcount)
"""
