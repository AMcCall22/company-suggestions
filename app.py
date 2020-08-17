import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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


# Connects to company_type collection in MongoDB for dropdown options
@app.route("/add_company", methods=["GET", "POST"])
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
    query = request.form.get("company_query")
    print(query)
    if query is None:
        return render_template("search_companies.html")
    else:
        company = mongo.db.companies.find({"$text": {"$search": query}})
    return render_template("all_companies_list.html", list_company=company)


@app.route("/edit_company/<company_id>", methods=["GET", "POST"])
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
        mongo.db.companies.update({"_id": ObjectId(company_id)}, submit_company)

    company = mongo.db.companies.find_one({"_id": ObjectId(company_id)})
    company_type = mongo.db.company_type.find()
    return render_template("edit_company.html", company=company, company_type=company_type)


@app.route("/delete_company/<company_id>")
def delete_company(company_id):
    mongo.db.companies.remove({"_id": ObjectId(company_id)})
    return redirect(url_for('list_company'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
