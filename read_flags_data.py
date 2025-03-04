import pandas as pd

raw_country_flags = pd.read_csv("flags.csv", sep=";",
                                   usecols=["name", 
                                   "image", 
                                   "landmass",
                                   "language",
                                   "religion"])
flags = raw_country_flags.copy()

flags = flags.astype({
       "name": "string",
       "image": "string",
       "landmass": int,
       "language": int,
       "religion": int,
})


# Rename columns for better readance and consistency
flags = flags.rename(columns={
                            "name":"CountryName",
                            "image":"ImageURL",
                            "landmass":"Continent",
                            "language":"CountryLanguage",
                            "religion":"CountryReligion"},
                     errors="raise")

# Named continents
flags.Continent[flags["Continent"] == 1] = "Americas"
flags.Continent[flags["Continent"] == 2] = "Americas"
flags.Continent[flags["Continent"] == 3] = "Europe"
flags.Continent[flags["Continent"] == 4] = "Africa"
flags.Continent[flags["Continent"] == 5] = "Asia"
flags.Continent[flags["Continent"] == 6] = "Oceania"

# Named languages
flags.CountryLanguage[flags["CountryLanguage"] == 1] = "English"
flags.CountryLanguage[flags["CountryLanguage"] == 2] = "Spanish"
flags.CountryLanguage[flags["CountryLanguage"] == 3] = "French"
flags.CountryLanguage[flags["CountryLanguage"] == 4] = "German"
flags.CountryLanguage[flags["CountryLanguage"] == 5] = "Slavic"
flags.CountryLanguage[flags["CountryLanguage"] == 6] = "Other Indo-European"
flags.CountryLanguage[flags["CountryLanguage"] == 7] = "Chinese"
flags.CountryLanguage[flags["CountryLanguage"] == 8] = "Arabic"
flags.CountryLanguage[flags["CountryLanguage"] == 9] = "Japanese/Turkish/Finnish/Magyar"
flags.CountryLanguage[flags["CountryLanguage"] == 10] = "Others"

# Named religions
flags.CountryReligion[flags["CountryReligion"] == 1] = "Other Christian"
flags.CountryReligion[flags["CountryReligion"] == 0] = "Catholic"
flags.CountryReligion[flags["CountryReligion"] == 2] = "Muslim"
flags.CountryReligion[flags["CountryReligion"] == 3] = "Buddhist"
flags.CountryReligion[flags["CountryReligion"] == 4] = "Hindu"
flags.CountryReligion[flags["CountryReligion"] == 5] = "Ethnic"
flags.CountryReligion[flags["CountryReligion"] == 6] = "Marxist"
flags.CountryReligion[flags["CountryReligion"] == 7] = "Other"

# Save in case I need to use it
flags.to_csv("flags-clean.csv", sep=",", index=False, header=True)
