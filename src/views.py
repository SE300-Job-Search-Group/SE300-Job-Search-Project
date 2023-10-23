from flask import Blueprint, render_template, request
from JobSearchObj import JobHandler

#Flask blueprint for views
views = Blueprint(__name__, "views")

#initializing jobHandler
job_handler = JobHandler()

@views.route("/home", methods=['GET', 'POST']) #defining route to home page
def home():
    #request to the home page
    if request.method == 'POST':
        #method is POST if the user uses the search bar
        query = request.form.get('query')
        keywords = query.split()

        #using the jobHandler
        matching_jobs = job_handler.searchDB(keywords)
        
        #page to display search results
        return render_template('search_results.html', jobs=matching_jobs)
    
    #home page is displayed if nothing is searched
    return render_template("index.html")

@views.route("/login") #defining the route to login page 
def login():
    return render_template("login.html")

@views.route("/profile") #defining the route to profile page 
def profile():
    return render_template("profile.html")

@views.route("/jobmatch") #defining the route to job match page 
def jobmatch():
    return render_template("jobMatch.html")

@views.route("/jobcompare") #defining the route to compare page 
def jobcompare():
    return render_template("jobCompare.html")

@views.route("/about") #defining the route to about page 
def about():
    return render_template("about.html")