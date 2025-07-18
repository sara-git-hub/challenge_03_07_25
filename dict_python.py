# -*- coding: utf-8 -*-
"""dict_python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1q2KyjDj-H0eNNiDeLZwgW3mC-gBamvsG

Challenge: Manipulation des dictionnaires Python
"""

First_dict = { "Appareil": "Laptop", "Marque": "IBM",
              "Carte mère": "MSI Z490", "Carte Graphique":"GeForce RTX 3070", "RAM": "16G", "Processeur": "Intel core i7-G11", "SSD": "1 To" }

First_dict["RAM"]="32G"

for keys in First_dict:
  print(keys)

for keys,value in First_dict.items():
  print(value)

for keys,value in First_dict.items():
  print(keys,":",value)

First_dict['Processeur'],First_dict['Carte Graphique']=First_dict['Carte Graphique'],First_dict['Processeur']

First_dict["Système d’exploitation"]= "Windows 10"

print(First_dict)

notes_eleves = { "Amine": 15.5, "Yassine": 19.0, "Reda": 14.2, "Malak": 8.7, "Manal": 20.0, "Ahmed": 7.5,"Saad": 11.3, "Hannae": 9.8 }

def part(notes_eleves):
    etudiant_admis={}
    etudiant_non_admis={}
    for etudiant,note in notes_eleves.items():
        if note>=10:
            etudiant_admis[etudiant]=note
        else:
            etudiant_non_admis[etudiant]=note
    return etudiant_admis,etudiant_non_admis

print(part(notes_eleves))

"""Challenge : Mise à Jour de Dictionnaires"""

def fusionner(dic1,dic2,dic3):
  dic0={}
  dic0.update(dic1)
  dic0.update(dic2)
  dic0.update(dic3)
  return dic0

dic1={"a":1,"b":2}
dic2={"a": 1,"c":3,"d":4}
dic3={"e":5,"f":6}
print(fusionner(dic1,dic2,dic3))

"""Challenge : Conversion de Deux Listes en Dictionnaire"""

list1=['a','b','c']
list2=[1,2,3]

def list_to_dict(list1,list2):
    liste=zip(list1,list2)
    return dict(liste)

print(list_to_dict(list1,list2))

"""Challenge : Tri d'un Dictionnaire par Valeur"""

etudiant_info=("Yasmine", 22, "Informatique", 17.4)
print(f"Prénom : {etudiant_info[0]}")
print(f"Âge : {etudiant_info[1]}")
print(f"Filière : {etudiant_info[2]}")
print(f"Moyenne générale : {etudiant_info[3]}")

#etudiant_info[0]="Sara"
# TypeError car le tuple est immuable

etudiant_info_part=etudiant_info[:2]
print(etudiant_info_part)

etudiant_info_sup=("Très Bien",2024)
etudiant_info_total=etudiant_info + etudiant_info_sup
print(etudiant_info_total)