from flask import Blueprint, request, session, render_template, redirect, url_for, flash
from jobSearchObj import JobHandler
from jobSearchObj import UserHandler

views = Blueprint(__name__, "views")
job_handler = JobHandler()
user_handler = UserHandler()

@views.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form.get('query')
        keywords = query.split()
        company = request.form.get('company')
        location = request.form.get('location')
        salary_min = request.form.get('salary_range')
        salary_max = request.form.get('salary_range')

        # Use job_handler.searchDB() with the filters
        matching_jobs = job_handler.searchDB(keywords, company, location, salary_min, salary_max)

        return render_template('search_results.html', jobs=matching_jobs)

    return render_template("index.html")

@views.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        keywords = [kw.strip() for kw in request.form.get("keywords").split(',')]
        skills = [skill.strip() for skill in request.form.get("skills").split(',')]
        city = request.form.get("city")
        state = request.form.get("state")
        min_salary = request.form.get("min_salary")
        max_salary = request.form.get("max_salary")

        # Input validation
        """if not (username and password and keywords and skills and city and state and min_salary and max_salary):
            flash("All fields are required.", "error")
            return redirect(url_for('views.register'))

        try:
            min_salary = int(min_salary)
            max_salary = int(max_salary)
        except ValueError:
            flash("Salary values must be valid integers.", "error")
            return redirect(url_for('views.register'))"""

        user_handler.createAccount(username, password, keywords, skills, city, state, min_salary, max_salary)
        return redirect(url_for('views.profile'))
        
    return render_template("register.html", registration_url=url_for('views.register'))

@views.route("/login", methods=['GET', 'POST'])  # Defining the route to the login page
def login():
    registration_url = url_for('views.register')
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if user_handler.login(username, password) is not False:
            # User login successful
            session['user_id'] = user_handler.curUser.getID() 
            return redirect(url_for('views.profile'))
        else:
            # User login failed, render the login page with an error message
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html", registration_url=registration_url)


@views.route("/profile") #defining the route to profile page 
def profile():
    if 'user_id' in session:
        username = user_handler.userUsername()
        keywords = user_handler.userKeywords()
        skills = user_handler.userSkills()
        location = user_handler.userLocation()
        salary_range = user_handler.userSalaryRange()

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
        if user_handler.updateAccount(user_id, new_location, new_salary_range, new_keywords, new_skills):
            # Profile update successful, you can redirect to the user's profile page or another page
            flash("Profile updated successfully.")
            return redirect(url_for('views.profile'))
        else:
            # Profile update failed, handle the error
            flash("Profile update failed. Please try again.")

    # If the request method is GET, display the profile editing form
    return render_template("edit_profile.html")

@views.route('/logout')
def logout():
    # Clear the user session data to log the user out
    session.clear()
    return redirect(url_for('views.login')) 

@views.route("/jobmatch") #defining the route to job match page 
def jobmatch():
    return render_template("jobMatch.html")

@views.route("/jobcompare") #defining the route to compare page 
def jobcompare():
    return render_template("jobCompare.html")

@views.route("/about") #defining the route to about page 
def about():
    return render_template("about.html")