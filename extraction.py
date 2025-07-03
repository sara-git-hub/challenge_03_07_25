import os
chemin=r"C:\Users\lenovo\Desktop\Simplon_Pyton_manip_fich"
for fichier in os.listdir(chemin):
    if fichier.lower().endswith(".txt"):
        print(fichier)
