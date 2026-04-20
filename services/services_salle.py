from Data.dao_salles import dataSalles

class ServiceSalle:

    def __init__(self):
        self.dao = dataSalles()

    def add_salle(self, salle):

        if salle.code == "" or salle.libelle == "" or salle.type_salle == "" or salle.capacite <= 0:
            return False, "Champs vides ou capacité invalide"

        
        existing = self.dao.get_one_salle(salle.code)
        if existing:
            return False, "Salle avec ce code existe déjà"

        try:
            self.dao.insert_salle(salle)
            return True, "Ajout réussi"
        except Exception as e:
            return False, f"Erreur lors de l'ajout: {e}"

    def update_salle(self, salle):

        if salle.code == "" or salle.libelle == "" or salle.type_salle == "" or salle.capacite <= 0:
            return False, "Champs vides ou capacité invalide"

        try:
            self.dao.update_salle(salle)
            return True, "Modification réussie"
        except Exception as e:
            return False, f"Erreur lors de la modification: {e}"

    def delete_salle(self, code):
        try:
            self.dao.delete_salle(code)
            return True, "Suppression réussie"
        except Exception as e:
            return False, f"Erreur lors de la suppression: {e}"

    