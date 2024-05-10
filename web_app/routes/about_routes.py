from flask import Blueprint, render_template, flash, redirect, url_for, request #, jsonify

from app.models.about import About

about_routes = Blueprint("about_routes", __name__)

@about_routes.route("/about")
def about():
    return render_template("about.html")

@about_routes.route("/about/create", methods=["POST"])
def create_about():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Process these details, e.g., save to database or send an email

    print("CREATE ABOUT FORM...")

    form_data = dict(request.form)
    print("FORM DATA:", form_data)
    name = form_data['name']
    email = form_data['email']
    message = form_data['message']

    try:
        params = {
            "name": name,
            "email": email,
            "message": message,
        }
        #order = Order(params)
        #order.save()
        # alternatively:
        About.create(params)

        flash(f"Message received!", "success")
        return render_template("about.html")
    except Exception as err:
        print(err)
        flash(f"Oops, something went wrong: {err}", "warning")
        return render_template("about.html")
