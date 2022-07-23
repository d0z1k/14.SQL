from flask import Flask

from blueprint_movies.views import blueprint_movies


app = Flask(__name__)
app.register_blueprint(blueprint_movies)

if __name__ == '__main__':
    app.run(debug=True)
