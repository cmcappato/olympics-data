import pandas as pd

raw_athletes = pd.read_csv("athlete_events.csv", sep=",")
athletes = raw_athletes.copy()
athletes = athletes.fillna(0)

athletes.columns


athletes = athletes.drop(columns="ID")

# Rename columns
athletes = athletes.rename(columns={
                        "Name": "AthleteName",
                        "Sex":"Gender",
                        "Team":"Country",
                        "City":"HostCity",
                        "NOC":"IOC"
                }, errors="raise")
athletes.info()

# Save to use later
athletes.to_csv("athletes-data-clean.csv", sep=",", index=False, header=True,quoting=1)
