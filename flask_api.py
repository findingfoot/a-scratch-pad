import flask
from flask import jsonify
from flask import request
app = flask.Flask(__name__)
app.config["DEBUG"] = True

telephone = [

    {'id': 0,
        'Name': "Prashant Kumar",
        'Number': "74574345",
        'Adress': "somewhere",
        'SSN': " 5643"},


    {
            'id':1,
            'Name': "koi aur",
            'Number': "702345235",
            'Adress': "nowhere",
            'SSN': " 3623"
    },

    {
                'id':2,
                'Name': "someone",
                'Number': "79397979",
                'Address': "maybe",
                'SSN': "24743"
    },
]
@app.route("/", methods = ['GET'])

def home():
    return "<h1>Creating a Flask Prototype</h1><p>This site is a prototype API for seeing how an API is created from scratch.</p>"


@app.route("/api/v1/resources/telephone/all", methods=["GET"])

def api_all():
    return jsonify(telephone)

#adding data filtering ability to our code
@app.route("/api/v1/resources/telephone", methods=["GET"])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No such Id exists in our records. "

    results = []

    for tele in telephone:
        if tele['id'] == id:
            results.append(tele)


    return jsonify(results)


app.run()
