from euc_import import Dataset
import pandas as pd

sediment = Dataset("chen_import", "sediment_individual.csv")
sediment_locations = sediment.get_locations()

biota = Dataset("chen_import", "biota_individual.csv")
biota_locations = biota.get_locations()

water = Dataset("chen_import", "water_individual.csv")
water_locations = water.get_locations()

unique_locations = []

for location in (sediment_locations + biota_locations + water_locations):
    if location not in unique_locations:
        unique_locations.append(location)

for location in unique_locations:
    location['biome_id'] = None
    location['biome_name'] = None
    location['environmental_feature_id'] = None
    location['environmental_feature_name'] = None

columns = unique_locations[0].keys()
df = pd.DataFrame(columns=columns)
    
for location in unique_locations:
    data = []

    for key in location.keys():
        data.append(location[key])

    df = df.append(pd.DataFrame(columns=columns, data=[data]), ignore_index=True)

df.to_csv("locations.csv", index=False)