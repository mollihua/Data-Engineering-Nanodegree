# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay_table"
user_table_drop = "DROP TABLE IF EXISTS user_table"
song_table_drop = "DROP TABLE IF EXISTS song_table"
artist_table_drop = "DROP TABLE IF EXISTS artist_table"
time_table_drop = "DROP TABLE IF EXISTS time_table"

# CREATE TABLES
# note: 
# songplay_table is the fact table. 
# The other tables are domain tables.
# In fact table, make sure foreign keys of fact table 
# (a.k.a. primary keys of domain tables) are NOT NULL.

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplay_table(
songplay_id SERIAL PRIMARY KEY NOT NULL,
start_time timestamp NOT NULL REFERENCES time_table(start_time),
user_id int NOT NULL REFERENCES user_table(user_id),
level varchar,
song_id varchar REFERENCES song_table(song_id),
artist_id varchar REFERENCES artist_table(artist_id),
session_id int, 
location varchar,
user_agent varchar)
""")


user_table_create = ("""CREATE TABLE IF NOT EXISTS user_table(
user_id int PRIMARY KEY NOT NULL,
first_name varchar,
last_name varchar,
gender varchar,
level varchar)
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS song_table(
song_id varchar PRIMARY KEY NOT NULL,
title varchar,
artist_id varchar,
year int,
duration float)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artist_table(
artist_id varchar PRIMARY KEY NOT NULL,
artist_name varchar,
location varchar,
latitude float,
longitude float)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time_table(
start_time timestamp PRIMARY KEY NOT NULL,
hour int,
day int,
week int,
month int,
year int,
weekday int)
""")



# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplay_table(
start_time,
user_id,
level,
song_id,
artist_id,
session_id, 
location,
user_agent)
VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT DO NOTHING
""")

user_table_insert = ("""INSERT INTO user_table(
user_id,
first_name,
last_name,
gender,
level)
VALUES(%s,%s,%s,%s,%s)
ON CONFLICT (user_id) DO UPDATE 
SET level=excluded.level
""")

song_table_insert = ("""INSERT INTO song_table(
song_id,
title,
artist_id,
year,
duration)
VALUES(%s,%s,%s,%s,%s)
ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""INSERT INTO artist_table(
artist_id,
artist_name,
location,
latitude,
longitude)
VALUES(%s,%s,%s,%s,%s)
ON CONFLICT DO NOTHING
""")


time_table_insert = ("""INSERT INTO time_table(
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

song_select = ("""
    SELECT song_id, artist_table.artist_id
    FROM song_table JOIN artist_table ON song_table.artist_id = artist_table.artist_id
    WHERE title = %s AND artist_name = %s AND duration = %s
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
