import sqlite3
import pprint as pp


class NetflixDAO:
    def __init__(self, nameDB: str) -> None:
        self.nameDB = nameDB

    # Database connection settings
    @staticmethod
    def _database_connection(name):
        """
        Create a database connection to the database.
        """
        with sqlite3.connect(name) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
        return cursor

    def db_execute(self, query):
        """Execute a query"""
        cursor = self._database_connection(self.nameDB)
        result = cursor.execute(query)
        return result

    def movies(self) -> list:
        """
        загружает всю базу
        """
        query = f"""SELECT * 
        FROM 'netflix'
        """
        movie_list = []
        result = self.db_execute(query).fetchall()
        for item in result:
            movie_list.append(dict(item))
        return movie_list

    def movie_by_name(self, name: str):
        """
        поиск по названию
        """
        query = f"""
        SELECT title, country, release_year, listed_in, description
        FROM 'netflix'
        WHERE title LIKE '%{name}%'
        ORDER BY release_year DESC
        LIMIT 1
        """

        result = self.db_execute(query).fetchall()
        for item in result:
            return dict(item)

    def movie_by_release_year_range(self, release_year1: int, release_year2: int) -> list:
        """
        поиск по диапазону лет выпуска.
        """
        query = f"""
        SELECT title, release_year
        FROM 'netflix'
        WHERE release_year
        BETWEEN {release_year1} AND {release_year2}
        LIMIT 100
        """

        movie_list = []
        result = self.db_execute(query).fetchall()
        for item in result:
            movie_list.append(dict(item))
        return movie_list

    def movie_by_rating(self, *ratings) -> list:
        """
        поиск по рейтингу
        """
        query = f"""
                SELECT title, rating, release_year
                FROM 'netflix'
                WHERE rating IN {ratings}
                ORDER BY release_year DESC
                LIMIT 100
                """

        movie_list = []
        result = self.db_execute(query).fetchall()
        for item in result:
            movie_list.append(dict(item))
        return movie_list

    def movie_by_genre(self, genre: str):
        """
        получает название жанра в качестве аргумента
        и возвращает 10 самых свежих фильмов в формате json.
        """
        query = f"""
                SELECT title, description
                FROM 'netflix'
                WHERE listed_in LIKE '%{genre}%'
                ORDER BY release_year DESC
                LIMIT 10
                """

        movie_list = []
        result = self.db_execute(query).fetchall()
        for item in result:
            movie_list.append(dict(item))
        return movie_list


    def get_actors(self, actor_1: str, actor_2: str):
        """
        Шаг 5, Актёры, сыгравшие в паре больше 2х раз
        """

        query = f"""
                SELECT cast
                FROM 'netflix'
                WHERE cast LIKE '%{actor_1}%' 
                AND cast LIKE '%{actor_2}%'
                """
        actors_all = []
        result = self.db_execute(query).fetchall()
        for movie in result:
            actors = movie[0].split(", ")
            actors_all.extend(actors)
        # Оставляем тех, кто встречается дважды
        actors_seen_twice = {actor for actor in actors_all if actors_all.count(actor) > 2} - {actor_1, actor_2}
        print(actors_seen_twice)



    def get_movie_info(self, type: str, year: int, genre: str):
        """
        Get info about a movie
        :param type: Type of movie
        :param year: year of the movie
        :param genre: genre of the movie
        """
        query = f"""
                SELECT description
                FROM 'netflix'
                WHERE type LIKE '%{type}%' 
                AND release_year == '{year}'
                AND listed_in LIKE '%{genre}%'
                """
        movie_list = []
        result = self.db_execute(query).fetchall()
        for item in result:
            movie_list.append(dict(item))
        return movie_list
