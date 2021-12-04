from flask import Flask


app = Flask(__name__)
# creates the flask
"""
def create_app():
    app = Flask(__name__)
    return app
"""
# The view function index() is linked to the main route using the app.route() decorator.
# When the main route is requested, Flask will serve the request by calling index() and using its return value as the response.

@app.route("/") # obviously the default page.
def index():
    return "Hello World!"
