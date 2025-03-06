import pandas as pd

raw_country_codes = pd.read_csv("country-codes.csv", sep=",")
codes = raw_country_codes.copy()

codes = codes.astype({
        "NOC": "string",
        "region": "string"
})

codes["regions"] = codes.apply(lambda row: f"{row['region']} ({row['notes']})" if pd.notna(row['notes']) and row['notes'] != '' else row['region'], axis=1)
codes = codes.drop(columns=["region","notes"])

codes = codes.rename(columns={
                        "NOC":"IOC",
                        "regions":"Country"},
                errors="raise")

# Save to use later
codes.to_csv("country-codes-clean.csv", sep=",", index=False, header=True, quoting=1)
