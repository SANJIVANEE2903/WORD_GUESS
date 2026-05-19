# database/score_db.py

import sqlite3


class ScoreDatabase:

    def __init__(self):

        self.connection = sqlite3.connect(
            "scores.db"
        )

        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute(

            '''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                score INTEGER
            )
            '''

        )

        self.connection.commit()

    def save_score(self, score):

        self.cursor.execute(

            "INSERT INTO scores(score) VALUES(?)",

            (score,)
        )

        self.connection.commit()

    def get_high_score(self):

        self.cursor.execute(

            "SELECT MAX(score) FROM scores"
        )

        result = self.cursor.fetchone()[0]

        return result if result else 0