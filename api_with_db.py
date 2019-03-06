import flask
from flask import jsonify, request
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def dict_read(cursor, row):
    d = {}
    for key, value in enumerate(cursor.description):
        d[value[0]] = row[key]
    return d


# by default response
@app.route('/', methods=['GET'])
def home():
    return "<h1>Creating a Flask Prototype</h1><p>This site is a prototype API for seeing " \
           "how an API is created from scratch" \
           " this time using <b>Database</b>.</p>"


# just parsing all information present on the database like a raw dump
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_read
    cur = conn.cursor()
    all_books = cur.execute('Select * from books;').fetchall()

    return jsonify(all_books)


# build in some error handling
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


# setup filter on books data

@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    query = "SELECT * FROM books where"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    if not (id or published or author):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_read
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)


app.run()
