import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_csv('data/boligdata.csv')

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

#Sjekker om en kategori dominerer kraftig
print(df["energimerke"].value_counts(dropna=False))
'''

# Baseline
df_dropna = df.copy().dropna()

# Gjennomsnitt for numeriske kolonner og modus for kategoriske kolonner
df_mean = df.copy()

numeriske = [
    "areal_m2",
    "byggeaar",
    "pris_kr"
]

kategoriske = [
    "energimerke"
]

df_mean[numeriske] = df_mean[numeriske].fillna(
    df_mean[numeriske].mean()
)

for kolonne in kategoriske:
    df_mean[kolonne] = df_mean[kolonne].fillna(
        df_mean[kolonne].mode()[0]
    )

# Median for numeriske kolonner og modus for kategoriske kolonner
df_median = df.copy()

df_median[numeriske] = df_median[numeriske].fillna(
    df_median[numeriske].median()
)

for kolonne in kategoriske:
    df_median[kolonne] = df_median[kolonne].fillna(
        df_median[kolonne].mode()[0]
    )

# Modus for alle kolonner med manglende verdier
df_mode = df.copy()

for kolonne in [
    "areal_m2",
    "byggeaar",
    "energimerke",
    "pris_kr"
]:
    df_mode[kolonne] = df_mode[kolonne].fillna(
        df_mode[kolonne].mode()[0]
    )

# Sjekker hvor mange manglende verdier som gjenstår etter hver metode
print("Dropna:")
print(df_dropna.isnull().sum())

print("Gjennomsnitt:")
print(df_mean.isnull().sum())

print("Median:")
print(df_median.isnull().sum())

print("Modus:")
print(df_mode.isnull().sum())

# Datatap
print("Originalt datasett:")
print(df.shape)

print("Dropna:")
print(df_dropna.shape)

# Påvirkning på fordelingen med de ulike metodene
print("Original:")
print(df.describe())

print("Dropna:")
print(df_dropna.describe())

print("Gjennomsnitt:")
print(df_mean.describe())

print("Median:")
print(df_median.describe())

print("Modus:")
print(df_mode.describe())