from flask import Flask

from blueprint_movies.views import blueprint_movies
from config import NAME_DB
from daoDB import NetflixDAO


app = Flask(__name__)
Database = NetflixDAO(NAME_DB)
app.register_blueprint(blueprint_movies)

if __name__ == '__main__':
    app.run(debug=True)
