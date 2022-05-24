from unicodedata import name
from flask import Blueprint, render_template, request, flash
from db_connection import *
from bottle import route, run, template, redirect, error, request
import json

# Länkar comments.py med main.py.
comments = Blueprint('comments', __name__)

#läser kommentarer från vår json fil
def read_comments_from_file():
    try:
        my_file = open('comments.json','r')
        comments = json.loads(my_file.read())
        my_file.close()

        return comments
    
    except FileNotFoundError:
        my_file = open('comments.json','w')
        my_file.write(json.dumps([]))
        my_file.close()

        return []


@route('/add_comment', method='POST')
def add_comment():
    #hämtar kommentarer från html mallen
    comment_text = getattr(request.forms, "comment_text")

    comments = read_comments_from_file()

    comments.append({
        "comment_text": comment_text
    })

    try:
        my_file = open('comments.json', 'w')
        my_file.write(json.dumps(comments,indent=4))
        my_file.close()
    except:
        print("Kommentar kunde inte läggas upp, testa igen senare")
    redirect("/")
