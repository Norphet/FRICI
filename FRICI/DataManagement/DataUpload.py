import pandas as pd
import pickle

rawdatabase = pd.read_excel(r'E:\Internet\Downloads\frici_data.xlsx')
print(rawdatabase)
print(rawdatabase.dtypes)

pickle.dump(rawdatabase, open("data.bin", "wb"))

# How to Import data:
# import pickle
# matrix = pickle.load(open("data.bin", "rb"))