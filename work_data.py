import sqlite3
import pandas as pd

conn = sqlite3.connect("football.db")

query = '''
SELECT 
    "utcDate",
    "homeTeam.name",
    "awayTeam.name",
    "score.fullTime.home",
    "score.fullTime.away"
FROM matches
LIMIT 10
'''
df = pd.read_sql(query, conn)

print(df)