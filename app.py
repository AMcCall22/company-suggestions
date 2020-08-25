import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Displays 4 most recently added companies on home page
@app.route("/")
@app.route("/show_company")
def show_company():
    company = mongo.db.companies.find().sort("_id", -1).limit(4)
    return render_template("companies.html", show_company=company)
    return render_template("all_companies.list.html", show_company=company)


# Display all companies as a list view
@app.route("/list_company")
def list_company():
    company = mongo.db.companies.find()
    return render_template("all_companies_list.html", list_company=company)


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        current_user = mongo.db.users.find_one(
            {"name": request.form.get("name").lower()}
        )
        if current_user:
            return redirect(url_for("registration"))

        registration = {
            "name": request.form.get("name").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(registration)

        session["user"] = request.form.get("name").lower()
        flash("You are now registered! Please log in.")
    return render_template("registration.html")


# User Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        current_user = mongo.db.users.find_one(
            {"name": request.form.get("name").lower()})

        if current_user:
            if check_password_hash(
                    current_user["password"], request.form.get("password")):
                session["user"] = request.form.get("name").lower()
                session["logged_in"] = True
                flash("You are now logged in!")
                return redirect(url_for("show_company"))
            else:
                flash("Incorrect Username or Password entered, please try again.")

        else:
            flash("Incorrect Username or Password entered, please try again.")
            return redirect(url_for("login"))

    return render_template("login.html")


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("Please log in to access here.")
            return redirect(url_for("login"))
    return wrap


# User Log Out
@app.route("/logout")
def logout():
    session.clear()
    flash("You're now logged out!")
    return redirect(url_for("login"))


# Connects to company_type collection in MongoDB for dropdown options
@app.route("/add_company", methods=["GET", "POST"])
@is_logged_in
def add_company():
    if request.method == "POST":
        company = {
            "company_type": request.form.get("company_type"),
            "company_name": request.form.get("company_name"),
            "sector": request.form.get("sector"),
            "description": request.form.get("description"),
            "url": request.form.get("url"),
            "remote": request.form.get("remote"),
            "level_of_positions": request.form.get("level_of_positions"),
        }
        mongo.db.companies.insert_one(company)
    company_type = mongo.db.company_type.find()
    return render_template("add_company.html", company_type=company_type)


# Search all companies and provide view of results
@app.route("/search_company", methods=["GET", "POST"])
def search_company():
    query1 = request.form.get("company_query")
    query2 = request.form.get("remote_option")
    print(type(query1))
    print(type(query2))
    if query1 is None:
        # Only carry out a checkbox search
        company = mongo.db.companies.find({"$text": {"$search": query2}})
        return render_template("search_companies.html")
    elif query2 is None:
        # Only carry out a text search
        company = mongo.db.companies.find({"$text": {"$search": query1}})
    else:
        # Carry out both checkbox and text search
        company = mongo.db.companies.find(
            {"$text": {"$search": ''.join(
                ["\"", query1, "\" \"", query2, "\""])}})
    return render_template("all_companies_list.html", list_company=company)


@app.route("/edit_company/<company_id>", methods=["GET", "POST"])
@is_logged_in
def edit_company(company_id):

    if request.method == "POST":
        submit_company = {
            "company_type": request.form.get("company_type"),
            "company_name": request.form.get("company_name"),
            "sector": request.form.get("sector"),
            "description": request.form.get("description"),
            "url": request.form.get("url"),
            "remote": request.form.get("remote"),
            "level_of_positions": request.form.get("level_of_positions"),
        }
        mongo.db.companies.update(
            {"_id": ObjectId(company_id)}, submit_company)

    company = mongo.db.companies.find_one({"_id": ObjectId(company_id)})
    company_type = mongo.db.company_type.find()
    return render_template(
        "edit_company.html", company=company, company_type=company_type)


@app.route("/delete_company/<company_id>")
@is_logged_in
def delete_company(company_id):
    mongo.db.companies.remove({"_id": ObjectId(company_id)})
    return redirect(url_for('list_company'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
