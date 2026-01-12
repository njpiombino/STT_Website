# Imports
from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

# My App
app = Flask(__name__)
Scss(app)

# Routes to Webpages
@app.route("/")
def index():
    return render_template("index.html")


# Runner and Debugger
if __name__ == "__main__":
    app.run(debug=True)