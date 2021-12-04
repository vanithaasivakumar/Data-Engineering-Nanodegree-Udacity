# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE songplays(
    songplay_id SERIAL PRIMARY KEY
    ,start_time TIMESTAMP
    ,user_id INT
    ,level VARCHAR(25)
    ,song_id VARCHAR(100)
    ,artist_id VARCHAR(100)
    ,session_id INT
    ,location VARCHAR(255)
    ,user_agent VARCHAR(255)
    ,FOREIGN KEY(start_time) REFERENCES time(start_time)
    ,FOREIGN KEY(user_id) REFERENCES users(user_id)
    ,FOREIGN KEY(song_id) REFERENCES songs(song_id)
    ,FOREIGN KEY(artist_id) REFERENCES artists(artist_id))
""")

user_table_create = ("""CREATE TABLE users(
    user_id INT PRIMARY KEY
    ,first_name VARCHAR(100)
    ,last_name VARCHAR(100)
    ,gender VARCHAR(100)
    ,level VARCHAR(25))
""")

artist_table_create = ("""CREATE TABLE artists(
    artist_id VARCHAR(100) PRIMARY KEY
    ,name VARCHAR(100)
    ,location VARCHAR(255)
    ,latitude NUMERIC
    ,longitude NUMERIC)
""")

song_table_create = ("""CREATE TABLE songs(
    song_id VARCHAR(100) PRIMARY KEY
    ,title VARCHAR(255)
    ,artist_id VARCHAR(100)
    ,year INT
    ,duration NUMERIC
    ,FOREIGN KEY(artist_id) REFERENCES artists(artist_id))
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

songplay_table_insert = ("""INSERT INTO songplays(
start_time,
user_id,
level,
song_id,
artist_id,
session_id,
location,
user_agent)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT DO NOTHING
""")

user_table_insert = ("""INSERT INTO users(
user_id,
first_name,
last_name,
gender,
level)
VALUES (%s,%s,%s,%s,%s)
ON CONFLICT(user_id) DO UPDATE SET LEVEL = EXCLUDED.LEVEL
""")

song_table_insert = ("""INSERT INTO songs(song_id, title, artist_id, year, duration) VALUES (%s, %s, %s,%s, %s) ON CONFLICT DO NOTHING""")

artist_table_insert = ("""INSERT INTO artists(
artist_id,
name,
location,
latitude,
longitude)
VALUES (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING
""")


time_table_insert = ("""INSERT INTO time(
start_time,
hour,
day,
week,
month,
year,
weekday)
VALUES(%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""SELECT song_id , artists.artist_id FROM songs JOIN artists ON songs.artist_id = artists.artist_id where title=%s AND name=%s AND duration=%s
""")

# QUERY LISTS

create_table_queries = [time_table_create,artist_table_create,song_table_create,user_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]