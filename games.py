
import sqlite3, json
from datetime import datetime

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

class Game:
    def __init__(self, user_id, timestamp, score):
        self.user_id = user_id
        self.timestamp = timestamp
        self.score = score


class Games:
    def __init__(self):
        pass

    @staticmethod
    def get_games(user_id):
        db = get_db_connection()
        games = db.execute(
            "SELECT * FROM games WHERE user_id = ?", (user_id,)
        ).fetchall()
        db.close()
        if not games:
            return None
        
        games_list = []
        for game in games:
            game = Game(
                user_id=game[0], timestamp=game[1], score=game[2]
            )
            games_list.append(game)
        
        return games_list

    @staticmethod
    def save_new_game(user_id, timestamp, score):
        db = get_db_connection()
        db.execute(
            "INSERT INTO games (user_id, timestamp, score) VALUES(?, ?, ?)", (user_id, timestamp, score)
        )
        db.commit()
        db.close()
