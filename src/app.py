from flask import Flask, redirect, url_for 
from views import views 

app = Flask(__name__, template_folder="templates") #initializing the application
app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__": #runs the application
    app.run(debug=True)



