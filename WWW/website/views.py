import imp
from flask import Blueprint, render_template
from db_connection import *

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/products') 
def product():
    return render_template("products.html")

