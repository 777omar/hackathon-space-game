import sqlite3

class Leaderboard:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def setup_leaderboard(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS leaderboard (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                score INTEGER NOT NULL
            )
        ''')
        self.connection.commit()

    def add_score(self, name, score):
        self.cursor.execute('INSERT INTO leaderboard (name, score) VALUES (?, ?)', (name, score))
        self.connection.commit()

    def get_leaderboard(self):
        self.cursor.execute('SELECT name, score FROM leaderboard ORDER BY score DESC')
        return self.cursor.fetchall()
