import sqlite3
import pprint as pp


class NetflixDAO:
    def __init__(self, nameDB: str) -> None:
        self.nameDB = nameDB

    # Database connection settings
    @staticmethod
    def _database_connection(name):
        with sqlite3.connect(name) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
        return cursor

    def db_execute(self, query):
        cursor = self._database_connection(self.nameDB)
        result = cursor.execute(query)
        return result

    def movies(self) -> list:
        query = f"""SELECT * 
        FROM 'netflix'
        """
        movie_list = []
        result = self.db_execute(query).fetchall()
        for item in result:
            movie_list.append(dict(item))
        return movie_list

    def movie_by_name(self, name: str):
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
