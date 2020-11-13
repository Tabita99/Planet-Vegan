import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home_page")
def home_page():
    # renders home page and get category list for both dropdowns
    categories = list(mongo.db.category.find())
    print("categories", categories)
    return render_template(
        "home.html", categories=categories,
        categories_one=mongo.db.category.find())


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        signUp = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(signUp)

        # put new user into session
        session["users"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile"))
    return render_template(
        # find categories to display both dropdowns
        "signup.html", categories=mongo.db.category.find(),
        categories_one=mongo.db.category.find())


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # put new user into session
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["users"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                            request.form.get("username")))
                return redirect(url_for(
                            "profile"))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for(
                    "login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template(
        # find categories to display both dropdowns
        "login.html", categories=mongo.db.category.find(),
        categories_one=mongo.db.category.find())


@app.route("/profile")
def profile():
    # grab the session user's username from db
    return render_template(
        # find categories to display both dropdowns
        "profile.html", recipes=mongo.db.recipes.find(),
        categories=mongo.db.category.find(),
        categories_one=mongo.db.category.find())


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("users")
    return redirect(url_for(
        # find categories to display both dropdowns
        "login", categories=mongo.db.category.find(),
        categories_one=mongo.db.category.find()))


@app.route("/category/<category_id>", methods=["GET"])
def category_recipes(category_id):
    # grabs the category id's from the db
    category = mongo.db.category.find_one({"_id": ObjectId(category_id)})
    print("category", category)
    recipes = mongo.db.recipes.find({"category_name": ObjectId(category_id)})
    return render_template(
        # find categories to display both dropdowns
        "categories_recipes.html", recipes=recipes, category=category,
        categories=mongo.db.category.find(),
        categories_one=mongo.db.category.find())


@app.route("/open_recipe/<recipe_id>")
def open_recipe(recipe_id):
    # grabs selected recipe from db
    get_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        # find categories to display both dropdowns
        "recipe.html", recipe=get_recipe, categories=mongo.db.category.find(),
        categories_one=mongo.db.category.find())


# CRUD functionality for the recipe collection

@app.route('/add_recipes')
def add_recipes():
    categories = list(mongo.db.category.find())
    return render_template(
        # find categories to display both dropdowns
        "addrecipes.html", categories=categories,
        categories_one=mongo.db.category.find())


@app.route('/submit_recipes', methods=["POST"])
def submit_recipes():
    # submitting recipes on website
    if request.method == "POST":
        recipe = {
          "category_name": ObjectId(request.form.get("category_name")),
          "image": request.form.get("image"),
          "recipe_name": request.form.get("recipe_name"),
          "recipe_description": request.form.get("recipe_description"),
          "time_to_cook": request.form.get("time_to_cook"),
          "prep_time": request.form.get("prep_time"),
          "serves": request.form.get("serves"),
          "ingredients": request.form.get("ingredients"),
          "method": request.form.get("method"),
          "user": session["users"],
          "credit": request.form.get("credit")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Added , Thank you!")
        return redirect(url_for('profile'))


@app.route('/edit_recipes/<recipe_id>', methods=["GET", "POST"])
def edit_recipes(recipe_id):
    # updating of existing recipes
    if request.method == "POST":
        recipe = {
          "category_name": ObjectId(request.form.get("category_name")),
          "image": request.form.get("image"),
          "recipe_name": request.form.get("recipe_name"),
          "recipe_description": request.form.get("recipe_description"),
          "time_to_cook": request.form.get("time_to_cook"),
          "prep_time": request.form.get("prep_time"),
          "serves": request.form.get("serves"),
          "ingredients": request.form.get("ingredients"),
          "method": request.form.get("method"),
          "user": session["users"],
          "credit": request.form.get("credit")
        }
        mongo.db.recipes.update(
            {'_id': ObjectId(recipe_id)}, recipe)
        flash("Recipe Edited , Thank you!")
        return redirect(url_for('profile'))
    the_recipe = mongo.db.recipes.find_one(
            {"_id": ObjectId(recipe_id)})
    return render_template(
        # find categories to display both dropdowns
        'editrecipe.html', recipe=the_recipe,
        categories=list(mongo.db.category.find()),
        categories_one=mongo.db.category.find())


@app.route('/delete_recipes/<recipe_id>')
def delete_recipes(recipe_id):
    # Allows for the deleting of recipes
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('profile'))


@app.route('/search', methods=['GET', 'POST'])
def search():
    # retrieve recipe based on searched words
    if request.method == "POST":
        query = request.form.get('query')
        recipes = mongo.db.recipes.find({'$text': {"$search": query}})
        print(query)
        print(recipes)
        return render_template(
            # find categories to display both dropdowns
            "search.html", recipes=recipes,
            categories=mongo.db.category.find(),
            categories_one=mongo.db.category.find())
    else:
        return render_template(
            # find categories to display both dropdowns
            'search.html', categories=mongo.db.category.find(),
            categories_one=mongo.db.category.find())


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)