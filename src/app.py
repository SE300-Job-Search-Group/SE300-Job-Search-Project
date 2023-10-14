from flask import Flask, redirect, url_for #importing Flask
from views import views #importing the views variable

app = Flask(__name__) #initializing the application
app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__": #runs the application
    app.run(debug=True)
