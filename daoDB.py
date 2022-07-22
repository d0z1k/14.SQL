import sqlite3


class NetflixDAO:
    def __init__(self, nameDB: str) -> None:
        self.nameDB = nameDB

    # Database connection settings
    def _database_connection(self, name):
        with sqlite3.connect(name) as connection:
            cursor = connection.cursor()
        return cursor

    def movies(self) -> list:
        query = f"""SELECT * FROM 'netflix'
        """
        cursor = self._database_connection(self.nameDB)
        result = cursor.execute(query)
        return result.fetchall()

    def movie_tit(self, tit: str) -> list:
        query = f"""
        SELECT title, director 
        FROM 'netflix'
        WHERE title LIKE :substring;
        """
        cursor = self._database_connection(self.nameDB)
        result = cursor.execute(query, {'substring': f'%{tit}%'})
        return result.fetchall()
