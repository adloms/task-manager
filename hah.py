import pandas as pd

df = pd.read_csv("pokemon.csv", index_col="Name")

#tall_pokemon = df[df["Height"] >= 2]
#heavy_pokemon = df[df["Weight"] > 100]
legendary_pokemon = df[df["Legendary"] == 1]
print(legendary_pokemon)