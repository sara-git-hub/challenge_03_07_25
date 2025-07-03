import os

#Challenge : Extraction et Traitement de Fichiers

chemin=r"C:\Users\lenovo\Desktop\Simplon_Pyton_manip_fich"

list_fichier=[]

for fichier in os.listdir(chemin):
    if fichier.lower().endswith(".txt"):
        print(fichier)
        list_fichier.append(fichier)
        
print(list_fichier)

for fichier in list_fichier:
    with open(fichier,'r') as f:
        print(f.read())

print("\n")

#Challenge : Recherche de Fichiers
import shutil

chemin2=r"C:\Users\lenovo\Desktop\Recherche_fichier\fichierRecherche.txt"

if os.path.exists(chemin2):
    with open(chemin2,'r') as f:
        print(f.read())

else:
    print("non trouvé!")

print("\n")
#Challenge : Copie Sélective de Fichiers

content=os.listdir()
print(content)

for fichier in content:
    if fichier.lower().endswith(".xlsx"):
        shutil.copy(fichier, r"C:\Users\lenovo\Desktop\Recherche_fichier")
        print(f"le fichier {fichier} a été copié")
print("\n")

#Challenge : Création de Répertoires

dossier="nouveau_repertoire"
os.makedirs(dossier)

liste_nom=["repertoire1","repertoire2","repertoire3"]

for fichier in liste_nom:
    os.chdir(r"C:\Users\lenovo\Desktop\Simplon_Pyton_manip_fich\nouveau_repertoire")
    os.makedirs(fichier)

#Challenge : Écriture de Fichiers

fichier_t=r"C:\Users\lenovo\Desktop\Simplon_Pyton_manip_fich\texte.txt"



with open(fichier_t,'w') as f:
    for ligne in range(5):
        f.write(f"ligne{ligne}\n")






    
