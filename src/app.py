from flask import Flask, redirect, url_for 
from views import views 

app = Flask(__name__, template_folder="templates") #initializing the application
app.register_blueprint(views, url_prefix="/")
app.secret_key = 'AeroSearch'

@app.route("/")
def index():
    #redirect from the root URL ("/") to the /home page
    return redirect(url_for('views.home'))

if __name__ == "__main__": #runs the application
    app.run(debug=True)



