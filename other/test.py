
from db.user import User

user = User.get(1)

print(user.games.get_games(1))

user.games.save_new_game(1, 1679936166, 10)

print(user.games.get_games(1))
