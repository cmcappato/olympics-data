import pandas as pd

raw_country_codes = pd.read_csv("country-codes.csv", sep=",")
codes = raw_country_codes.copy()

codes.info()

# List columns
codes.columns

# Delete columns I don"t need
codes = codes.drop(labels=["FIFA", "Dial", "ISO3166-1-Alpha-3", "MARC", "is_independent",
        "ISO3166-1-numeric", "GAUL", "FIPS", "WMO", "ITU", "DS", "ISO3166-1-Alpha-2",
        "UNTERM Spanish Formal", "Global Code", "Intermediate Region Code", "official_name_fr", "UNTERM French Short",
        "ISO4217-currency_name", "UNTERM Russian Formal", "UNTERM English Short", 
        "ISO4217-currency_alphabetic_code", "Small Island Developing States (SIDS)", 
        "UNTERM Spanish Short", "ISO4217-currency_numeric_code", "UNTERM Chinese Formal",
        "UNTERM French Formal", "UNTERM Russian Short", "M49", "Sub-region Code", "official_name_es",
        "Region Code", "official_name_ar", "ISO4217-currency_minor_unit", "Languages",
        "UNTERM Arabic Formal", "UNTERM Chinese Short", "Global Name", "Continent",
        "Land Locked Developing Countries (LLDC)", "Intermediate Region Name", "UNTERM English Formal", "official_name_cn", "ISO4217-currency_country_name",
        "Least Developed Countries (LDC)", "UNTERM Arabic Short", "Sub-region Name", 
        "official_name_ru", "TLD", "Geoname ID", "CLDR display name", "EDGAR", "wikidata_id"], axis=1)


# Delete record if IOC is empty
codes = codes.dropna(subset=["IOC"])

codes = codes.rename(columns={
                            "official_name_en":"CountryName",
                            "Region Name":"Continent"},
                    errors="raise")

# Save in case I need to use it
codes.to_csv("country-codes-clean.csv", sep=",", index=False, header=True)
