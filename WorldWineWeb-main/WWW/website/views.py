import this
from unittest import result
from flask import Blueprint, render_template, request, flash, redirect, url_for
from db_connection import *

# Definierar views som blueprints för att vi ska kunna använda det som templates.
views = Blueprint('views', __name__)

# Routar ålderkontroll.
@views.route('/')
def start():
    return render_template("age_control.html")

@views.route('/omoss', methods=['GET', 'POST'])
def omoss():

        if request.method == 'POST':
            search_product = request.form.get("searchfunction")
            print(search_product)
            print("Products found!")
            cur = conn.cursor()
            insert_script = "SET search_path = 'WorldWineWeb', am4404, public; select searchProduct('%s')" % (search_product)
            print(insert_script)
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
    
        
            if search_product != '':
                print(rows)
                return render_template("products.html", rows=rows)

        return render_template("omoss.html")

@views.route("/comments")
def comments():
    return render_template("comments.html")

# Routar hem.
@views.route('/home', methods=['GET', 'POST'])
def home():
    print("Home route was called")

    if request.method == 'POST':
        search_product = request.form.get("searchfunction")
        print(search_product)
        cur = conn.cursor()
        insert_script = "SET search_path = 'WorldWineWeb', am4404, public; select searchProduct('%s')" % (search_product)
        print(insert_script)
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
   
    
        if search_product != '':
            print(rows)
            return render_template("products.html", rows=rows)
            


    return render_template("index.html")

# Routar till info om varför man inte kommer åt hemsidan
@views.route('/decline')
def decline():
    return render_template("decline.html")

# Routar produktsida 
@views.route("/products/<productid>")
def show_product(productid):
    print("produktid i route produktsida" + productid)
    cur = conn.cursor()
    insert_script = "SET search_path = 'WorldWineWeb', am4404, public; select * from product where productid ='%s'" % (productid)
    cur.execute(insert_script)
    print(insert_script + "här")
    records = cur.fetchall()
    conn.commit()
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
      
    
    cur = conn.cursor()
    insert_script1 = "SET search_path = 'WorldWineWeb', am4404, public; select getproductcomments('%s')" % (productid)
    cur.execute(insert_script1)
    print(insert_script1 + "här")
    records = cur.fetchall()
    for comments in records:
        print(comments)
    conn.commit()
                
    return render_template("product_page.html", productid = productid, rows=rows)


# Routar produktkatalogen 
@views.route('/products', methods=['GET', 'POST'])
def product():
    
    print("Products found!")
    cur = conn.cursor()
    insert_script = 'SET search_path = "WorldWineWeb", am4404, public; Select getproducts(20)'
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

    




