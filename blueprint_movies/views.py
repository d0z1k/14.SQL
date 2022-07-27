import string

from flask import jsonify, Blueprint

from blueprint_movies.DAO.daoDB import NetflixDAO
from config import NAME_DB

Database = NetflixDAO(NAME_DB)
blueprint_movies = Blueprint("blueprint_movies", __name__)


@blueprint_movies.route('/')
def index():
    return jsonify(Database.movies())


@blueprint_movies.route('/movie/<string:name>')
def movie_by_title(name: str):
    return jsonify(Database.movie_by_name(name))


@blueprint_movies.route('/movie/<int:year1>/to/<int:year2>')
def movie_by_year(year1: int, year2: int):
    return jsonify(Database.movie_by_release_year_range(year1, year2))


# @blueprint_movies.route('/movie/children')
# def movie_by_rating():
#     return jsonify(Database.movie_by_rating(G))
