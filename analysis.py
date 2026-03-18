import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Verbindung zur Datenbank
conn = sqlite3.connect("football.db")

# SQL Query 
query = '''
SELECT 
    "homeTeam.name" as team,
    SUM("score.fullTime.home") as goals
FROM matches
GROUP BY "homeTeam.name"
ORDER BY goals DESC
'''

# Daten laden
df = pd.read_sql(query, conn)

print(df)

# Diagramm erstellen
df.plot(kind="barv", x="team", y="goals")

plt.title("Top 10 Teams nach Toren (Heimspiele)")
plt.xlabel("Tore")
plt.ylabel("Team")

plt.show()
