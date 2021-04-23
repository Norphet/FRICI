import pandas as pd
import pickle
matrix = pickle.load(open("data.bin", "rb"))

def beolvas(adatbazis):
    ingredient=[]
    quantity=[]
    receptek=[]
    key= input("Do you want to give more ingredients, y for yes n for no")
    szamlalo = 0
    while key=='y':
        ingredient.append(input("Type in the ingredient that you have"))
        quantity.append(input("Type in the quantity that you have"))
        counter1=0
        counter2=0

        for i in range(adatbazis.shape[1]):
            if adatbazis.columns[i] == ingredient[szamlalo]:
                counter1=counter1+1

        key = input("Do you want to give more ingredients, y for yes n for no")
        if key=='y':
            szamlalo = szamlalo + 1
    for i in range(adatbazis.shape[0]):
            if (adatbazis[ingredient[szamlalo]][i] !=0) & (adatbazis[ingredient[szamlalo-1]][i] !=0):
                receptek.append(adatbazis['name'][i])
    return receptek



matrix = pickle.load(open("data.bin", "rb"))
print(matrix)
print(beolvas(matrix))


