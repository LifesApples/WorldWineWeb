import this
from unittest import result
from flask import Blueprint, render_template, request, flash
from db_connection import *

# Definierar views som blueprints för att vi ska kunna använda det som templates.
views = Blueprint('views', __name__)

# Routar ålderkontroll.
@views.route('/')
def start():
    return render_template("age_control.html")

# Routar hem.
@views.route('/home', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        searchfunction = request.form.get("Searchfunction")
        print("Sökfunktionen: " + str(searchfunction))

        try:
            cur = conn.cursor()
            insert_script= "SET search_path = 'WorldWineWeb', am4404, public; select * from product where productname LIKE '%s'" % (searchfunction)
            print("Testing: " + insert_script)
            cur.execute(insert_script)
            rows = []
            rows = cur.fetchall()
            conn.commit()
            print("Results: " + cur.rowcount)
            print(rows[0])


            if cur.rowcount == 1:
                    return render_template("product_page.html", productid = rows[0], rows=rows)
            else:
                    return render_template("products.html", rows=rows)
        except:
            pass

    """
            if request.method == 'POST':
            searchfunction = request.form.get("searchfunction")
            print("Sökfunktion: " + searchfunction)

            try:
                
                insert_script = "SET search_path = 'WorldWineWeb', am4404, public; select * from product where productname LIKE '&s' '%'"  %(searchterm)
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
    """        
    return render_template("index.html")

# Routar till info om varför man inte kommer åt hemsidan
@views.route('/decline')
def decline():
    return render_template("decline.html")

# Routar produktsida 
@views.route("/products/<productid>")
def show_product(productid):
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
      
    
                     
    return render_template("product_page.html", productid = productid, rows=rows)


# Routar produktkatalogen 
@views.route('/products')
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




