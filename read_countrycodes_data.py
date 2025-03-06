import pandas as pd

raw_country_codes = pd.read_csv("country-codes.csv", sep=",")
codes = raw_country_codes.copy()

codes = codes.astype({
        "NOC": "string",
        "region": "string"
})

codes = codes.drop(columns=["notes"])

codes = codes.rename(columns={
                        "NOC":"IOC",
                        "region":"Country"},
                errors="raise")

# Save to use later
codes.to_csv("country-codes-clean.csv", sep=",", index=False, header=True, quoting=1)
