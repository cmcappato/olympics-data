import pandas as pd

raw_olympics = pd.read_csv("olympics-data.csv", sep=";")
oly = raw_olympics.copy()
oly = oly.fillna(0)

# Format data
oly = oly.astype({
        "Name": "string",
        "Sex": "string",
        "Age": int,
        "Height": int,
        "Name": "string",
        "Weight": float,
        "Team": "string",
        "NOC": "string",
        "Games": "string",
        "Year": "string",
        "Season": "string",
        "City": "string",
        "Sport": "string",
        "Event": "string",
        "Medal": int
})

oly.shape # Check size

# Rename columns
oly = oly.rename(columns={
                        "Name": "AthleteName",
                        "Sex":"Gender",
                        "Team":"CountryName",
                        "City":"HostCity",
                        "NOC":"IOC"
                }, errors="raise")
oly.info()

# Save to use later
oly.to_csv("olympics-data-clean.csv", sep=",", index=False, header=True)
