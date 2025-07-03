#Gestion d’un compte bancaire en POO

class CompteBancaire:
    def __init__(self, nom_proprietaire: str, solde =0.0):
        self.nom_proprietaire=nom_proprietaire
        self.solde=solde

    def deposer(self,montant):
        self.solde+=montant

    def retirer(self,montant):
        if self.solde<montant:
            print("solde insuffisant")
        else:
            self.solde-=montant
            
    def afficher_solde(self):
        return self.solde

print("challenge compte bancaire")
c1=CompteBancaire("Toto",100)
c1.deposer(1000)
c1.retirer(100)
print(f"le solde est {c1.solde}")
print("\n")


#Challenge :  Système de gestion d’école

from abc import ABC, abstractmethod

class Personne(ABC):
    def __init__(self,nom,prenom,age):
        self.nom=nom
        self.prenom=prenom
        self.age=age

    @abstractmethod
    def afficher_infos(self):
        pass

class Etudiant(Personne):
    
    def __init__(self,nom,prenom,age,matricule, notes=[]):
        super().__init__(nom,prenom,age)
        self.matricule=matricule
        self.notes=notes

    def ajouter_note(self,note):
        self.notes.append(note)

    def moyenne(self):
        return sum(self.notes)/len(self.notes)

    def afficher_infos(self):
        print(f"Nom:{self.nom}\nPrenom:{self.prenom}\nAge: {self.age}\nMatricule:{self.matricule}")
    
print("test classe étudiant")
etudiant1=Etudiant("Susan","Mayer",21,"ABC123")
etudiant1.ajouter_note(10)
etudiant1.ajouter_note(10)
print(f"la moyenne de {etudiant1.prenom} est : {etudiant1.moyenne()}")
print("\n")

class Enseignant(Personne):
    
    def __init__(self,nom,prenom:str,age:int,specialite,salaire):
        super().__init__(nom,prenom,age)
        self.specialite=specialite
        self._salaire=float(salaire)

    @property
    def salaire(self):
        return self._salaire
    

    @salaire.setter
    def salaire(self, nouveau_salaire):
        if not isinstance(nouveau_salaire,(float,int)):
            raise TypeError("le salaire doit être numérique")
        nouveau_salaire = float(nouveau_salaire)
        if nouveau_salaire <= 0:
            raise ValueError("Le salaire doit être positif")
        self._salaire = nouveau_salaire
    
    
    
    def afficher_infos(self):
        print(f"Nom:{self.nom}\nPrenom:{self.prenom}\nAge: {self.age}\nSpecialité:{self.specialite}\nSalaire:{self._salaire}")

print("test classe enseigant")
enseignant1=Enseignant("Dupond","Toto",40,"maths",20000)
enseignant1.salaire=25000
enseignant1.afficher_infos()
print("\n")

    
class Ecole:
    
    def __init__(self,nom,liste_etudiants=[],liste_enseignants=[]):
        self.nom=nom
        self.liste_etudiants=liste_etudiants
        self.liste_enseignants=liste_enseignants

    def ajouter_etudiant(self,etudiant):
        self.liste_etudiants.append(etudiant)

    def ajouter_enseignant(self,enseignant):
        self.liste_etudiants.append(enseignant)

    def afficher_tous_les_membres(self) :
        for etudiant in self.liste_etudiants:
            etudiant.afficher_infos()

        for enseignant in self.liste_enseignants:
            enseignant.afficher_infos()
            
        
print("test classe école")
ecole1=Ecole("Simplon")
ecole1.ajouter_etudiant(etudiant1)
ecole1.ajouter_enseignant(enseignant1)
ecole1.afficher_tous_les_membres()

        
