# DROP TABLES

songplay_table_drop = "DROP TABLE songsplay"
user_table_drop = "DROP TABLE users"
song_table_drop = "DROP TABLE song"
artist_table_drop = "DROP TABLE artist"
time_table_drop = "DROP TABLE time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE songplay(
    songplay_id INT PRIMARY KEY
    ,start_time TIMESTAMP
    ,user_id INT
    ,level VARCHAR(25)
    ,song_id INT
    ,artist_id INT
    ,session_id INT
    ,location VARCHAR(255)
    ,user_agent VARCHAR(255)
    ,FOREIGN KEY(start_time) REFERENCES time(start_time)
    ,FOREIGN KEY(user_id) REFERENCES users(user_id)
    ,FOREIGN KEY(song_id) REFERENCES song(song_id)
    ,FOREIGN KEY(artist_id) REFERENCES artist(artist_id))
""")

user_table_create = ("""CREATE TABLE users(
    user_id INT PRIMARY KEY
    ,first_name VARCHAR(100)
    ,last_name VARCHAR(100)
    ,gender VARCHAR(100)
    ,level VARCHAR(25))
""")

artist_table_create = ("""CREATE TABLE artist(
    artist_id INT PRIMARY KEY
    ,name VARCHAR(100)
    ,location VARCHAR(255)
    ,latitude NUMERIC
    ,longitude NUMERIC)
""")

song_table_create = ("""CREATE TABLE song(
    song_id INT PRIMARY KEY
    ,title VARCHAR(255)
    ,artist_id INT
    ,year INT
    ,duration NUMERIC
    ,FOREIGN KEY(artist_id) REFERENCES artist(artist_id))
""")

time_table_create = ("""CREATE TABLE time(
    start_time TIMESTAMP UNIQUE
    ,hour INT
    ,day INT
    ,week INT
    ,month INT
    ,year INT
    ,weekday INT)
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [time_table_create,artist_table_create,song_table_create,user_table_create,songplay_table_create   ]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]