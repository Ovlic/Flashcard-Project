CREATE TABLE user (
  user_id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  profile_pic TEXT NOT NULL
);

CREATE TABLE stats (
  user_id TEXT NOT NULL,
  total INTEGER NOT NULL,
  first_try INTEGER NOT NULL,
  average INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE games (
-- user_id, timestamp, score
  user_id TEXT NOT NULL,
  timestamp INTEGER NOT NULL,
  score REAL NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user(user_id)
);