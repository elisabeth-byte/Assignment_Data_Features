import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
df = pd.read_csv('data/vaerdata.csv')

#Klassifiserer datasettet, ser hvordan datasetett ser ut før en setter opp modell

'''
print(df.head(10)) #printer 10 første rader av alle kolonner
print(df.columns) #printer navnet på kolonnene
print("Size of dataset")
print(df.shape) #printer str på datasettet: antall rader og kolonner
print("Antall rader per kolonne med manglende data:")
print(df.isnull().sum()) #printer hvor mange verdier som mangler i hver kolonne

print(df.dtypes)
print("Prosentandel manglende data")
print((df.isnull().sum() / len(df) * 100).round(2))

# Skriver ut statistisk oppsummering av de numeriske kolonnene
# (antall verdier, gjennomsnitt, standardavvik, min, max og kvartiler)
print(df.describe())

# Viser de første radene hvor xxx mangler for å undersøke mønstre i de manglende verdiene
print("Viser de første radene hvor hver kolonne mangler data")
print(df[df["temperatur_c"].isnull()].head())
print(df[df["vind_ms"].isnull()].head())
print(df[df["nedbor_mm"].isnull()].head())
'''

# Baseline
df_dropna = df.copy().dropna()
# Gjennomsnitt
df_mean = df.copy().fillna(df.mean(numeric_only=True))
# Median
df_median = df.copy().fillna(df.median(numeric_only=True))
# Lineær interpolasjon
df_interp = df.copy()
df_interp.iloc[:, 1:] = df_interp.iloc[:, 1:].interpolate()

# Sjekker hvor mange manglende verdier som gjenstår etter hver metode
print("Dropna:")
print(df_dropna.isnull().sum())

print("Gjennomsnitt:")
print(df_mean.isnull().sum())

print("Median:")
print(df_median.isnull().sum())

print("Interpolasjon:")
print(df_interp.isnull().sum())

#Datatap
print("Originalt datasett:")
print(df.shape)

print("Dropna:")
print(df_dropna.shape)

#Påvirkning på fordelingen med de ulike metodene
print("Original:")
print(df.describe())

print("Dropna:")
print(df_dropna.describe())

print("Gjennomsnitt:")
print(df_mean.describe())

print("Median:")
print(df_median.describe())

print("Interpolasjon:")
print(df_interp.describe())

#plot
