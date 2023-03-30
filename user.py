from flask_login import UserMixin
import sqlite3
from stats import Stats
from games import Games


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


class User(UserMixin):
    def __init__(self, id_, name, email, profile_pic):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic
        self.stats = Stats
        self.games = Games

    @staticmethod
    def get(user_id):
        db = get_db_connection()
        user = db.execute(
            "SELECT * FROM user WHERE user_id = ?", (user_id,)
        ).fetchone()
        db.close()
        if not user:
            return None

        user = User(
            id_=user[0], name=user[1], email=user[2], profile_pic=user[3]
        )
        return user

    @staticmethod
    def get_from_email(email):
        db = get_db_connection()
        user = db.execute(
            "SELECT * FROM user WHERE email = ?", (email,)
        ).fetchone()
        db.close()
        if not user:
            return None

        user = User(
            id_=user[0], name=user[1], email=user[2], profile_pic=user[3]
        )
        return user

    @staticmethod
    def create(id_, name, email, profile_pic):
        db = get_db_connection()
        db.execute(
            "INSERT INTO user (user_id, name, email, profile_pic)"
            " VALUES (?, ?, ?, ?)",
            (id_, name, email, profile_pic),
        )
        db.commit()
        db.close()
