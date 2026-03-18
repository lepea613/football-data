import pandas as pd
import sqlite3

#Csv-Dateil laden
df = pd.read_csv("bundesliga_matches.csv")

#Verbindung zur Datenbank herstellen
conn = sqlite3.connect("football.db")

#Daten in SQL speichern
df.to_sql("matches", conn, if_exists="replace", index=False)

print("Datenbank erstellt")