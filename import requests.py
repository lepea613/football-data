import requests
import pandas as pd

# Bundesliga Code = BL1
url = "https://api.football-data.org/v4/competitions/BL1/matches"

headers = {
    "X-Auth-Token": "c6075638fd23453b8b8ee6156fc7c89d"
}

response = requests.get(url, headers=headers)

# Prüfen ob Anfrage erfolgreich war
if response.status_code == 200:
    data = response.json()

    matches = data["matches"]
    df = pd.json_normalize(matches)

    df.to_csv("bundesliga_matches.csv", index=False)
    print("Daten erfolgreich geladen!")
    print(data)
else:
    print("Fehler:", response.status_code)