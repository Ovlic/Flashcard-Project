
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


class Stats:
    def __init__(self, user_id, total, first_try, average):
        self.user_id = user_id
        self.total = total
        self.first_try = first_try
        self.average = average

    @staticmethod
    def get_stats(user_id):
        db = get_db_connection()
        stats = db.execute(
            "SELECT * FROM stats WHERE user_id = ?", (user_id,)
        ).fetchone()
        db.close()
        if not stats:
            print("None :(")
            return None
        
        stats = Stats(
            user_id=stats[0],  total=stats[1], first_try=stats[2], average=stats[3]
        )
        return stats

    def create_stats(id_,):
        db = get_db_connection()
        db.execute(
            "INSERT INTO stats (user_id, total, first_try, average) VALUES (?, ?, ?, ?)", 
            (id_, 0, 0, 0),
        )
        db.commit()
        db.close()

    @staticmethod
    def update_stats(user_id, score, first_try):
        print("user_id: ", user_id)
        db = get_db_connection()
        stats = db.execute(
            "SELECT * FROM stats WHERE user_id = ?", (user_id,)
        ).fetchone()
        db.close()
        if not stats:
            print("User not found, creating stats...")
            Stats.create_stats(user_id)
            print("Created stats for user, rerunning function...")
            return Stats.update_stats(user_id, score, first_try)
        
        stats = Stats(
            user_id=stats[0], total=stats[1], first_try=stats[2], average=stats[3]
        )
        stats.total += 1
        if first_try:
            stats.first_try += 1
        stats.average = round(((stats.average * (stats.total - 1) + score) / stats.total), 2)
        db = get_db_connection()
        db.execute(
            "UPDATE stats SET total = ?, first_try = ?, average = ? WHERE user_id = ?",
            (stats.total, stats.first_try, stats.average, user_id),
        )
        db.commit()
        db.close()
