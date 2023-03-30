import sqlite3, json

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
user_id = 1
games = [{"timestamp": 1679936166, "score": 5}, {"timestamp": 1679936166, "score": 8}]

cur.execute("INSERT INTO user (user_id, name, email, profile_pic) VALUES (?, ?, ?, ?)",
            (user_id, 'Test', 'test@test.com', 'test.jpg')
            )

cur.execute("INSERT INTO stats (user_id, total, first_try, average) VALUES (?, ?, ?, ?)",
            (user_id, 1, 1, 5)
)
for game in games:
    cur.execute("INSERT INTO games (user_id, timestamp, score) VALUES(?, ?, ?)", (user_id, game['timestamp'], game['score']))

connection.commit()
connection.close()