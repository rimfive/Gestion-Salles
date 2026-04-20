class salle:
    def __init__(self, code, libelle, type_salle, capacite):
        self.code = code
        self.libelle = libelle
        self.type_salle = type_salle
        self.capacite = capacite

    def afficher(self):
        print(f"Code: {self.code}")
        print(f"Libellé: {self.libelle}")
        print(f"Type de salle: {self.type_salle}")
        print(f"Capacité: {self.capacite}")
        print()
    def get_code(self):
        return self.code
    def get_libelle(self):
        return self.libelle