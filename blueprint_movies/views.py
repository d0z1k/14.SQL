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


@blueprint_movies.route('/movie/children')
def movie_by_rating_children():
    return jsonify(Database.movie_by_rating('G', 'empty'))


@blueprint_movies.route('/movie/family')
def movie_by_rating_family():
    return jsonify(Database.movie_by_rating('G', 'PG', 'PG-13'))


@blueprint_movies.route('/movie/adult')
def movie_by_rating_adult():
    return jsonify(Database.movie_by_rating('R', 'NC-17'))


@blueprint_movies.route('/movie/genre/<string:genre>')
def movie_by_genre(genre: str):
    return jsonify(Database.movie_by_genre(genre))
