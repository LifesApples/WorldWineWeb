import this
from flask import Blueprint, render_template
from db_connection import *

# Definierar views som blueprints för att vi ska kunna använda det som templates.
views = Blueprint('views', __name__)

# Routar hem.
@views.route('/')
def home():
    return render_template("index.html")

@views.route("/products/<productid>")
def show_product(productid):
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
    insert_script = 'SET search_path = "WorldWineWeb", am4404, public; Select getproducts(10)'
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
    return render_template("products.html", rows=rows)




@views.route("/prodcts/<product_id>")
def movie_details(movie_id): 
    '''
    Route för att hämta information och tillgänglighet för film. - ALi
    '''
    """
    country = (request.args.get('country') or "se").lower() # Hämtar land från get parametern or default se(Sverige)
    ssl._create_default_https_context =  ssl._create_unverified_context
    conn = requests.urlopen(get_movie_URL(movie_id))
    json_data = json.loads(conn.read())
    network = rq.request('GET', url, headers=headers, params=get_query_string(movie_id, country))
    conn2 = requests.urlopen(get_movie_credits(movie_id))
    conn3 = requests.urlopen(get_recommendations(movie_id))
    json_data2 = json.loads(conn2.read())
    json_data3 = json.loads(conn3.read())
    return render_template('movie.html', data=json_data, network_data=json.loads(network.text), data2=json_data2, data3=json_data3, country=country)
    """

