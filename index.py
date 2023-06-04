# Import of all the library used in this project
from flask import Flask, render_template, request, session, redirect
from flask_session import Session

# Configure app
app = Flask(__name__)

# Configuration Of Auto Reload Of All The Templates
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Taking user data to make the portfolio
@app.route("/", methods=["GET", "POST"])
def get_info():
    if request.method=="POST":
        fname=request.form.get("fname")
        lname=request.form.get("lname")
        email=request.form.get("email")
        phone=request.form.get("phone")
        domain=request.form.getlist("domain")
        occupation=request.form.get("occupation")
        selfdesc=request.form.get("selfdesc")
        expdesc=request.form.get("expdesc")
        skill=request.form.getlist("skill")
        skilldesc=request.form.getlist("skilldesc")
        github=request.form.get("github")
        linkedin=request.form.get("linkedin")
        twitter=request.form.get("twitter")
        blog=request.form.get("blog")
        portfolio=request.form.get("portfolio")
        degree=request.form.getlist("degree")
        startdate=request.form.get("startdate")
        enddate=request.form.get("enddate")
        company=request.form.getlist("company")
        startyear=request.form.get("startyear")
        endyear=request.form.get("endyear")
        
        # Converted the single element into many for best use

        splitskilldesc=skilldesc[0].split(",")
        splitsdomain=domain[0].split(",")
        splitdegree=degree[0].split(",")
        splitcompany=company[0].split(",")      

        # Storing the user data into session for easy access

        session["fname"] = fname
        session["lname"] = lname
        session["email"] = email
        session["phone"] = phone
        session["domain"] = splitsdomain
        session["occupation"] = occupation
        session["selfdesc"] = selfdesc
        session["expdesc"] = expdesc
        session["skill"] = skill
        session["skilldesc"] = splitskilldesc
        session["github"] = github
        session["linkedin"] = linkedin
        session["twitter"] = twitter
        session["blog"] = blog
        session["portfolio"] = portfolio
        session["degree"] = splitdegree
        session["startdate"] = startdate
        session["enddate"] = enddate
        session["company"] = splitcompany
        session["startyear"] = startyear
        session["endyear"] = endyear
        
        # Redirecting as per selected portfolio
        if portfolio == "1":
            return redirect("/portfolio1")
        else:
            return "Coming Soon"
        
    return render_template("detail_form.html")

@app.route("/portfolio1", methods=["GET", "POST"])
def portfolio_one():
    return render_template("index.html")

