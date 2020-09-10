import os
from flask import Flask, flash, render_template, redirect, request, \
    session, url_for

from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, \
    check_password_hash
from functools import wraps
if os.path.exists('env.py'):
    import env

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


@app.route('/')
@app.route('/show_company')
def show_company():
    # Display 4 most recently added companies on home page
    company = mongo.db.companies.find().sort('_id', -1).limit(3)
    return render_template('companies.html', show_company=company)


@app.route('/list_company')
def list_company():
    """
    Display all companies in collection in card format
    Pagination inspiration -
    https://github.com/DarilliGames/flaskpaginate/blob/master/app.py
    """
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    # Limit of 6 to be shown on each page
    per_page = 6
    offset = (page - 1) * per_page
    # Get the total values to be used later
    total = mongo.db.companies.find().count()
    # Get all the companies from mongodb
    company = mongo.db.companies.find().sort('_id', -1)
    # Paginate the companies found
    paginatedCompanies = company[offset:offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='materialize')
    return render_template(
        'all_companies_list.html',
        list_company=company,
        companies=paginatedCompanies,
        page=page,
        per_page=per_page,
        pagination=pagination,
        )


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    """
    Registration page for new users
    Code inspiration from CI tutor
    https://www.youtube.com/watch?v=Sfkg3358Igc&feature=youtu.be
    """
    if request.method == 'POST':
        current_user = \
            mongo.db.users.find_one({'name': request.form.get('name').lower()})
        if current_user:
            return redirect(url_for('registration'))
        registration = {"name": request.form.get("name").lower(),
                        "password": generate_password_hash(
                        request.form.get("password"))
                        }
        mongo.db.users.insert_one(registration)

        session['user'] = request.form.get('name').lower()
        flash('You are now registered! Please log in.')
    return render_template('registration.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    User Log In
    Code inspiration taken from Traversy Media
    https://www.youtube.com/watch?v=QEMtSUxtUDY
    """
    if request.method == 'POST':
        current_user = mongo.db.users.find_one(
            {"name": request.form.get("name").lower()})
        if current_user:
            if check_password_hash(current_user['password'],
                                   request.form.get('password')):
                session['user'] = request.form.get('name').lower()
                session['logged_in'] = True
                flash('You are now logged in!')
                return redirect(url_for('show_company'))
            else:
                flash('Incorrect Username or Password entered.')
        else:
            flash('Incorrect Username or Password entered, please try again.')
            # return redirect(url_for("login"))
    return render_template('login.html')


def is_logged_in(f):
    """
    A check to tell the user if they are logged in or not
    Code inspiration taken from Traversy Media
    https://www.youtube.com/watch?v=QEMtSUxtUDY
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Please log in to add a new company.')
            return redirect(url_for('login'))
    return wrap


@app.route('/logout')
def logout():
    # User Log Out
    session.clear()
    flash("You're now logged out!")
    return redirect(url_for('login'))


@app.route('/add_company', methods=['GET', 'POST'])
@is_logged_in
def add_company():
    # Add new company
    if request.method == 'POST':
        company = {
            'company_type': request.form.get('company_type'),
            'company_name': request.form.get('company_name'),
            'sector': request.form.get('sector'),
            'description': request.form.get('description'),
            'url': request.form.get('url'),
            'remote': request.form.get('remote'),
            'level_of_positions': request.form.get('level_of_positions'),
            }
        mongo.db.companies.insert_one(company)
        flash('Company successfully added!')
        return redirect(url_for('list_company'))

    company_type = mongo.db.company_type.find()
    return render_template('add_company.html',
                           company_type=company_type)


@app.route('/search_company', methods=['GET', 'POST'])
def search_company():
    """
    Search all companies and provide view of results
    Allow a text search and/or radio button search
    Pagination had to be removed due to complexity.
    Still referenced due to the return of all_companies_list.html
    """
    # Gather user search criteria from search_company.html
    query1 = request.form.get('company_query')
    query2 = request.form.get('remote_option')
    query3 = request.form.get('role_option')
    # Initialise "queryString" and render search page on first visit
    if query1 is None:
        queryString = ''
        return render_template('search_companies.html')
    else:
        queryString = ''.join(['"', query1, '"'])
    # Concatenate radio button responses to queryString
    if query2 is not None:
        queryString = ''.join([queryString, ' "', query2, '"'])
    if query3 is not None:
        queryString = ''.join([queryString, ' "', query3, '"'])
    # Execute mongodb query based on compiled queryString
    company = mongo.db.companies.find({"$text": {"$search": queryString}})
    # Show no results
    if company.count() == 0:
        flash('No results found. Please search again!')

    # Pagination override to remove from function
    page = 1
    per_page = 1000
    offset = (page - 1) * per_page
    total = company.count()
    paginatedCompanies = company[offset:offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='materialize')
    return render_template(
        'all_companies_list.html',
        list_company=company,
        companies=paginatedCompanies,
        page=page,
        per_page=per_page,
        pagination=pagination,
        )


@app.route('/edit_company/<company_id>', methods=['GET', 'POST'])
@is_logged_in
def edit_company(company_id):
    # Allow logged in user to edit companies already in the database
    if request.method == 'POST':
        submit_company = {
            'company_type': request.form.get('company_type'),
            'company_name': request.form.get('company_name'),
            'sector': request.form.get('sector'),
            'description': request.form.get('description'),
            'url': request.form.get('url'),
            'remote': request.form.get('remote'),
            'level_of_positions': request.form.get('level_of_positions'),
            }
        mongo.db.companies.update({'_id': ObjectId(company_id)},
                                  submit_company)
        flash('Company successfully updated!')
        return redirect(url_for('list_company'))
    company = mongo.db.companies.find_one({'_id': ObjectId(company_id)})
    company_type = mongo.db.company_type.find()
    return render_template('edit_company.html', company=company,
                           company_type=company_type)


@app.route('/delete_company/<company_id>')
@is_logged_in
def delete_company(company_id):
    # Allow logged in users to delete companies already in the database
    mongo.db.companies.remove({'_id': ObjectId(company_id)})
    flash('Company deleted!')
    return redirect(url_for('list_company'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
