import pandas as pd
import matplotlib.pyplot as plt

raw_olympics = pd.read_csv("olympics-data.csv", sep=";")
oly = raw_olympics.copy()
oly = oly.fillna(0)

# Format data
oly["Name"] = oly["Name"].astype('string')
oly["Sex"] = oly["Sex"].astype('string')
oly["Age"] = oly["Age"].astype(int) 
oly["Height"] = oly["Height"].astype(int)
oly["Weight"] = oly["Weight"].astype(float)
oly["Team"] = oly["Team"].astype('string')
oly["NOC"] = oly["NOC"].astype('string')
oly["Games"] = oly["Games"].astype('string')
oly["Year"] = oly["Year"].astype(int)
oly["Season"] = oly["Season"].astype('string')
oly["City"] = oly["City"].astype('string')
oly["Sport"] = oly["Sport"].astype('string')
oly["Event"] = oly["Event"].astype('string')
oly["Medal"] = oly["Medal"].astype(int)

oly.shape
oly = oly.rename(columns={
                        "Name": "AthleteName",
                        "Sex":"Gender",
                        "Team":"CountryName",
                        "City":"HostCity",
                        "NOC":"IOC"
                }, errors="raise")
oly.info()

oly.to_csv("olympics-data-clean.csv", sep=",", index=False, header=True)


# Males with medals
MalesWithMedal = oly.loc[(oly['Gender'] == 'M') & (oly['Medal'] != 0)].shape[0]
MalesWithoutMedal = oly.loc[(oly['Gender'] == 'M') & (oly['Medal'] == 0)].shape[0]

plt.title("Males winners vs. no winners")
plt.pie(x=[MalesWithMedal,oly['Gender'].value_counts()[0]], colors=["red","green"])
plt.show()

