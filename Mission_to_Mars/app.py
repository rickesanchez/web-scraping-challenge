# import necessary libraries
from flask import Flask, render_template

#import pymongo

# create instance of Flask app
app = Flask(__name__)

#conn = 'mongodb://localhost:27017'

#client = pymongo.MongoClient(conn)

# create route that renders index.html template
@app.route("/")
def echo():

    return render_template("index.html", text="Hey, it works!")

if __name__ == "__main__":
    app.run(debug=True)