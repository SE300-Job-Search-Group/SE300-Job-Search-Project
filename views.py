from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/home") #defining the route to the home page
def home():
    return render_template("index.html")

@views.route("/login") #defining the route to login page (incomplete)
def login():
    return render_template("index.html")