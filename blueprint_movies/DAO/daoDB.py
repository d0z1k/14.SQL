import sqlite3
import pprint


class NetflixDAO:
    def __init__(self, nameDB: str) -> None:
        self.nameDB = nameDB

    # Database connection settings
    def _database_connection(self, name):
        with sqlite3.connect(name) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
        return cursor

    def db_execute(self, query):
        cursor = self._database_connection(self.nameDB)
        result = cursor.execute(query)
        return result


    def movies(self) -> list:
        query = f"""SELECT * FROM 'netflix'
        """
        cursor = self._database_connection(self.nameDB)
        result = cursor.execute(query)
        return result.fetchall()

    def movie_by_name(self, name: str):
        query = f"""
        SELECT title, country, MAX(release_year), listed_in, description
        FROM 'netflix'
        WHERE title LIKE '%{name}%'
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

    # def movie_by_rating(self, rate) -> list:
    #     query = f"""
    #             SELECT title, rating, release_year
    #             FROM 'netflix'
    #             WHERE rating IN {rate}
    #             LIMIT 100
    #             """
    #
    #     cursor = self._database_connection(self.nameDB)
    #     result = cursor.execute(query)
    #     return result.fetchall()

    # pprint(movie_by_release_year_range(2009, 2019))
    # pprint(NetflixDAO(movie_by_name('Alive')))
