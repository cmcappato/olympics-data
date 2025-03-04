import pandas as pd

raw_country_codes = pd.read_csv("country-codes.csv", sep=",", 
                                usecols=["IOC", 
                                        "official_name_en", 
                                        "Region Name", 
                                        "Capital"])
raw_olympics = pd.read_csv("olympics-data-clean.csv", sep=",")
codes = raw_country_codes.copy()

codes.info()

codes = codes.astype({
        "IOC": "string",
        "official_name_en": "string",
        "Region Name": "string",
        "Capital": "string"
})

# Delete record if IOC is empty
codes = codes.dropna(subset=["IOC"])
codes.shape # Check size

# Merge with olympics archive to remove IOCs that are not present
codes = codes.merge(raw_olympics[["IOC"]], on="IOC", how="inner")
codes.shape # Check size

# Remove all duplicates, as I only need the information one time
codes = codes.drop_duplicates(subset=["IOC"])
codes.shape # Check size

codes = codes.rename(columns={
                        "official_name_en":"CountryName",
                        "Region Name":"Continent"},
                errors="raise")

# Save to use later
codes.to_csv("country-codes-clean.csv", sep=",", index=False, header=True, quoting=1)
