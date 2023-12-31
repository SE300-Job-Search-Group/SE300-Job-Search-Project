from flask import Blueprint, request, session, render_template, redirect, url_for
from jobSearchObj import JobHandler, UserHandler, CompanyMatch, Company

views = Blueprint(__name__, "views")
job_handler = JobHandler()
user_handler = UserHandler()
match_company = CompanyMatch()

@views.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form.get('query')
        tags = query.split()
        company = request.form.get('company')
        city = request.form.get('city')
        state = request.form.get('state')
        radius = request.form.get('radius')  # Get radius without converting to int yet
        salary_min = int(request.form.get('salary_min'))
        salary_max = int(request.form.get('salary_max'))

        # Check if both city and state are provided before using the radius
        if city and state:
            radius = int(radius) 
        else:
            radius = None  

        job_handler.searchDB(tags, company, city, state, radius, salary_min, salary_max)
        print(tags, type(tags))
        return redirect(url_for('views.search_results'))

    return render_template("index.html")


@views.route("/search_results", methods=['GET'])
def search_results():
    jobs = job_handler.getJobs()
    print(jobs)

    return render_template('search_results.html', jobs=jobs)


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

    if 'user_id' in session:
        keywords = user_handler.userKeywords()
        skills = user_handler.userSkills()
        city = user_handler.userCity()
        state = user_handler.userState()
        minSal = str(user_handler.userMinSalary())
        maxSal = str(user_handler.userMaxSalary())
        keywords_prefill = ""
        skills_prefill = ""
        for kw in keywords:
            keywords_prefill = keywords_prefill + kw+','
        
        for skill in skills:
            skills_prefill = skills_prefill + skill+','

    if request.method == 'POST':
        
        # Get the updated profile information from the form
        new_keywords = [kw.strip() for kw in request.form.get("new_keywords").split(',')]
        new_skills = [skill.strip() for skill in request.form.get("new_skills").split(',')] 
        new_city = request.form.get("new_city")
        new_state = request.form.get("new_state")
        new_minSal = request.form.get("new_salary_min")
        new_maxSal = request.form.get("new_salary_max")
    
        # Call the updateUser method to update the user's profile
        user_handler.updateAccount(new_keywords, new_skills, new_city, new_state, new_minSal, new_maxSal)
        # Profile update successful, you can redirect to the user's profile page or another page
        return redirect(url_for('views.profile'))
        

    # If the request method is GET, display the profile editing form
    return render_template("edit_profile.html", keywords=keywords_prefill,skills = skills_prefill,city = city,state = state, minSal = minSal, maxSal = maxSal)

@views.route('/logout')
def logout():
    # Clear the user session data to log the user out
    session.clear()
    user_handler.logout()
    return redirect(url_for('views.login')) 

@views.route('/company_match', methods=['GET', 'POST'])
def company_match():
    if request.method == 'POST':
        company1 = request.form.get('company1')
        company2 = request.form.get('company2')

        # Handling the conversion to integers with error handling
        try:
            work_life_balance = int(request.form['workLifeBalance'])
            compensation = int(request.form['compensation'])
            job_security = int(request.form['jobSecurity'])
            management = int(request.form['management'])
            culture = int(request.form['culture'])
            print(work_life_balance, type(work_life_balance))
        except (KeyError, ValueError) as e:
            # Handle the case where the form input is missing or not an integer
            return "Error: Please provide valid integer values for the ratings."

        return redirect(url_for('views.company_match_results',
                                company1=company1,
                                company2=company2,
                                work_life_balance=work_life_balance,
                                compensation=compensation,
                                job_security=job_security,
                                management=management,
                                culture=culture))

    return render_template('company_match.html')


@views.route('/company_match_results', methods=['GET', 'POST'])
def company_match_results():
    if request.method == 'POST':
        # Retrieve data from the submitted form
        company1 = request.form.get('company1')
        company2 = request.form.get('company2')
        work_life_balance = request.form.get('workLifeBalance')
        compensation = request.form.get('compensation')
        job_security = request.form.get('jobSecurity')
        management = request.form.get('management')
        culture = request.form.get('culture')

        # Check if any of the values retrieved are None before converting to int
        if None in (work_life_balance, compensation, job_security, management, culture):
            return "Error: Please provide values for all ratings."

        # Convert the retrieved values to integers
        try:
            work_life_balance = int(work_life_balance)
            compensation = int(compensation)
            job_security = int(job_security)
            management = int(management)
            culture = int(culture)
        except ValueError:
            return "Error: Please provide valid integer values for the ratings."

        # Call the scoreCompany method passing the retrieved variables
        matched_companies = match_company.scoreCompany(
            company1, company2, work_life_balance, compensation, job_security, management, culture)
      
        # Retrieve Company objects based on company names
        company1Obj = Company().findCompany(matched_companies[0])
        company2Obj = Company().findCompany(matched_companies[1])

        # Store matched_companies in the session
        session['matched_companies'] = matched_companies
    
        # Pass the matched companies to the template
        return render_template('company_match_results.html', company1Obj=company1Obj, company2Obj=company2Obj)

    return "Error: This route only accepts POST requests."


@views.route('/job_match', methods=['GET', 'POST'])
def job_match():
    
    matched_companies = session.get('matched_companies')
    matched_jobs = JobHandler().searchTags(matched_companies[0])

    return render_template('job_match.html', matched_companies=matched_companies, matched_jobs=matched_jobs)

@views.route("/about")  
def about():
    return render_template("about.html")