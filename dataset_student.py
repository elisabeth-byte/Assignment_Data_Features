import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_csv('data/studentdata.csv')

#Klassifiserer datasettet, ser hvordan datasetett ser ut før en setter opp modell

print(df.head(10)) #printer 10 første rader av alle kolonner
print(df.columns) #printer navnet på kolonnene
print("Size of dataset")
print(df.shape) #printer str på datasettet: antall rader og kolonner
print("Antall rader per kolonne med manglende data:")
print(df.isnull().sum()) #printer hvor mange verdier som mangler i hver kolonne