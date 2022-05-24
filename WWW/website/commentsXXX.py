from unicodedata import name
from flask import Blueprint, render_template, request, flash
from db_connection import *
from bottle import route, run, template, redirect, error, request
import json

@route('/new_comment', method='GET')
def add_comment():
    if request.GET.save:
        comment = request.GET.user_comment.strip()
        rating = request.GET.user_rating.strip()
        conn