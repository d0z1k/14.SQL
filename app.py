from flask import Flask, jsonify

from config import NAME_DB
from daoDB import NetflixDAO

app = Flask(__name__)
Database = NetflixDAO(NAME_DB)


@app.route('/')
def index():
    return jsonify(Database.movies())


@app.route('/movie/<string:title>')
def movie_by_title(title: str):
    return jsonify(Database.movie_tit(title))


if __name__ == '__main__':
    app.run(debug=True)
