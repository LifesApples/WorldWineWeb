import this
from flask import Blueprint, render_template
from db_connection import *

# Definierar views som blueprints för att vi ska kunna använda det som templates.
views = Blueprint('views', __name__)

# Routar ålderkontroll.
@views.route('/')
def start():
    return render_template("age_control.html")

# Routar hem.
@views.route('/home')
def home():
    return render_template("index.html")

@views.route('/decline')
def decline():
    return render_template("decline.html")

# Routar produktsida 
@views.route("/products/<productid>")
def show_product(productid):
    cur = conn.cursor()
    insert_script = 'SET search_path = "WorldWineWeb", am4404, public; Select getproducts(5)'
    cur.execute(insert_script)
    records = cur.fetchall()
    data = []
    data = list(records)
    rows = []
    #Skapar en lista i en lista där den innre listan innehåller värden för 1 produkt.
    for i in enumerate(data):
        #Formatterar texten från databasen
        splitColumns = str(i).split(",")
        splitColumns = [j.replace('"', '') for j in splitColumns]
        splitColumns = [j.replace('(', '') for j in splitColumns] 
        splitColumns = [j.replace(')', '') for j in splitColumns] 
        splitColumns = [j.replace("'", '') for j in splitColumns]
        #Lägger till listan i en lista för att skapa en produktkatalog
        rows.append(splitColumns)
      
    conn.commit()
                     
    return render_template("product_page.html", productid = productid, rows=rows)


# Routar produktkatalogen 
@views.route('/products')
def product():
    print("Products found!")
    cur = conn.cursor()
    insert_script = 'SET search_path = "WorldWineWeb", am4404, public; Select getproducts(10)'
    cur.execute(insert_script)
    records = cur.fetchall()
    data = []
    data = list(records)
    rows = []
    for i in enumerate(data):
        ##Lägger till värden för en produkt i en lista
        splitColumns = str(i).split(",")
        splitColumns = [j.replace('"', '') for j in splitColumns]
        splitColumns = [j.replace('(', '') for j in splitColumns]
        splitColumns = [j.replace(')', '') for j in splitColumns]
        splitColumns = [j.replace("'", '') for j in splitColumns] 
        ###Lägger till listan i en lista
        rows.append(splitColumns)
      
    conn.commit()
    return render_template("products.html", rows=rows)




