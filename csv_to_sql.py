"""
Ce code permet d’enregistrer dans un fichier texte .sql l’ensemble des instructions permettant d’ajouter à une relation les données contenues dans un
fichier .csv
"""

import csv

def csv_to_list(fichier):
    f = open(fichier, 'r')
    lect = csv.reader(f, delimiter = ";")
    data = [l for l in lect]
    attributs = data[0]
    data = data[1:]
    f.close()
    return data, attributs

def attributs_to_str(attributs):
    attributs_str = ""
    for e in attributs:
        attributs_str += e + ","
    attributs_str = attributs_str[:-1]
    return attributs_str


def csv_to_sql(fichier_csv):

    nom_fichier_sql = fichier_csv[:-4]

    data, attributs = csv_to_list(fichier_csv)

    attributs_str = attributs_to_str(attributs)

    types = []

    for e in attributs:
        t = input("type de l'attribut " + e + " (str ou int): ")
        types.append(t)

    f = open(nom_fichier_sql + '.sql','w')

    debut_ligne = "INSERT INTO " + nom_fichier_sql + " (" + attributs_str + ") VALUES ("

    for e in data:
        f.write(debut_ligne)
        for i in range (len(attributs)):
            if types[i] == "str" and i!=(len(attributs)-1):
                f.write("'" + e[i] + "'" + ",")
            elif types[i] == 'int' and i!=(len(attributs)-1):
                f.write(e[i])
                f.write(",")
            
            if types[i] == "str" and i==(len(attributs)-1):
                f.write( "'" + e[i] + "'")
            elif types[i] == 'int' and i==(len(attributs)-1):
                f.write(e[i])
        f.write(");\n")
    
    return


csv_to_sql("Client.csv .csv")




    
            
    




    

