import this
from typing import Counter
from flask import Blueprint, render_template
from db_connection import *

# Definierar views som blueprints för att vi ska kunna använda det som templates.
views = Blueprint('views', __name__)

# Routar hem.
@views.route('/')
def home():
    return render_template("index.html")


@views.route("/products/<productid>")
def show_article(productid):
    """Displays a single article (loaded from a text file)."""
    cur = conn.cursor()
    insert_script = 'SET search_path = "WorldWineWeb", am4404, public; Select getproducts(5)'
    cur.execute(insert_script)
    records = cur.fetchall()
    data = []
    data = list(records)
    columns = []
    rows = []
    for i in enumerate(data):
        ##Adds product attributes to a list
        splitColumns = str(i).split(",")
        splitColumns = [j.replace('"', '') for j in splitColumns] # remove quote from each element
        splitColumns = [j.replace('(', '') for j in splitColumns] # remove quote from each element
        splitColumns = [j.replace(')', '') for j in splitColumns] # remove quote from each element
        splitColumns = [j.replace("'", '') for j in splitColumns] # remove quote from each element
        print("Check: ",splitColumns)
        ##Adds the product with its attributes to a new row
        rows.append(splitColumns)
      
    conn.commit()
                     
    return render_template("product_page.html", productid = productid, rows=rows)


@views.route('/products')
def product():
    print("Products found!")
    cur = conn.cursor()
    insert_script = 'SET search_path = "WorldWineWeb", am4404, public; Select getproducts(5)'
    cur.execute(insert_script)
    records = cur.fetchall()
    data = []
    data = list(records)
    columns = []
    rows = []
    for i in enumerate(data):
        ##Adds product attributes to a list
        splitColumns = str(i).split(",")
        splitColumns = [j.replace('"', '') for j in splitColumns] # remove quote from each element
        splitColumns = [j.replace('(', '') for j in splitColumns] # remove quote from each element
        splitColumns = [j.replace(')', '') for j in splitColumns] # remove quote from each element
        splitColumns = [j.replace("'", '') for j in splitColumns] # remove quote from each element
        #print("Check: ",splitColumns)
        ##Adds the product with its attributes to a new row
        rows.append(splitColumns)
      
    conn.commit()
    return render_template("products.html", rows=rows)


