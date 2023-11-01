from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from jobSearchObj import JobHandler
from jobSearchObj import User
from jobSearchObj import UserHandler

views = Blueprint(__name__, "views")
job_handler = JobHandler()
user = User()
user_handler = UserHandler()

@views.route("/home", methods=['GET', 'POST']) #defining route to home page
def home():
    #check is user is logged in
    user_is_logged_in = 'user.id' in session

    if request.method == 'POST':
        #method is POST if the user uses the search bar
        query = request.form.get('query')
        keywords = query.split()

        # using the jobHandler
        matching_jobs = job_handler.searchDB(keywords)
        
        #TODO develop the page to show the matching jobs
        return render_template('search_results.html', jobs=matching_jobs)
    
    # home page is displayed if nothing is searched
    return render_template("index.html")

@views.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # User creation
        location = request.form.get("location")
        min_salary = request.form.get("min_salary")
        max_salary = request.form.get("max_salary")
        keywords = request.form.getlist("keywords")  # If using checkboxes for keywords
        skills = request.form.getlist("skills")  # If using checkboxes for skills

        # Create the new user and handle any errors during user creation
        if user.newUser(username, password, location, min_salary, max_salary, keywords, skills):
            # User creation successful, redirect to the "edit_profile" page
            return redirect(url_for('views.profile'))
        else:
            # User creation failed, handle the error (e.g., display an error message)
            error_message = "User registration failed. Please try again."
            return render_template("register.html", registration_url=url_for('register'), error=error_message)

    # If the request method is GET, display the registration form
    return render_template("register.html", registration_url=url_for('views.register'))


@views.route("/login", methods=['GET', 'POST'])  # Defining the route to the login page
def login():
    registration_url = url_for('views.register')
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if user_handler.login(username, password):
            # User login successful
            # Store user's ID in the session
            session['user_id'] = user_handler.curUser.getID() 
            return redirect(url_for('views.profile'))
        else:
            # User login failed, render the login page with an error message
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html", registration_url=registration_url)


@views.route("/profile") #defining the route to profile page 
def profile():
    if 'user_id' in session:
        username = user.getUsername()
        keywords = user.getKeywords()
        skills = user.getSkills()
        location = user.getLocation()
        salary_range = user.getSalaryRange()

        return render_template("profile.html", username=username, keywords=keywords, skills=skills, location=location, salary_range=salary_range)
    else:
        return redirect(url_for('views.login')) 

@views.route("/edit_profile", methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
        # Get the user's ID from the session
        user_id = session.get('user_id')

        # Get the updated profile information from the form
        new_location = request.form.get("new_location")
        new_salary_range = request.form.get("new_salary_range")
        new_keywords = request.form.getlist("new_keywords")  # If using checkboxes for keywords
        new_skills = request.form.getlist("new_skills")  # If using checkboxes for skills

        # Call the updateUser method to update the user's profile
        if user_handler.updateUser(user_id, new_location, new_salary_range, new_keywords, new_skills):
            # Profile update successful, you can redirect to the user's profile page or another page
            flash("Profile updated successfully.")
            return redirect(url_for('views.profile'))
        else:
            # Profile update failed, handle the error
            flash("Profile update failed. Please try again.")

    # If the request method is GET, display the profile editing form
    return render_template("edit_profile.html")

#Future work

@views.route("/jobmatch") #defining the route to job match page 
def jobmatch():
    return render_template("jobMatch.html")

@views.route("/jobcompare") #defining the route to compare page 
def jobcompare():
    return render_template("jobCompare.html")

@views.route("/about") #defining the route to about page 
def about():
    return render_template("about.html")