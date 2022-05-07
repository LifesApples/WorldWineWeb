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
    records = cur.fetchall()
    columns = []
    columns = list(records)

    columns = str(columns).split(",")
    for i in columns:
        print("Next value is:")
        print(i)

      
    ##print("Returned: ", records)
    conn.commit()
    return render_template("products.html", content=records)




