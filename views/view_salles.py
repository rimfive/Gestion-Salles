from Data.dao_salles import dataSalles
from models.salle import salle

class servicesSalle:
    def __init__(self):
        self.dao = dataSalles()

    def add_salle(self, salle):
        if not salle.code or not salle.libelle or not salle.type_salle or not salle.capacite:
            return False, "Tous les champs sont obligatoires"
        
        if salle.capacite < 1:
            return False, "La capacité doit être un nombre positif"
        
        self.dao.insert_salle(salle)
        return True, "Salle ajoutée avec succès"
    
    def update_salle(self, salle):
        if salle.code == "" or salle.libelle == "" or salle.type_salle == "" or salle.capacite == "":
            return False, "Tous les champs sont obligatoires"
        
        if salle.capacite < 1:
            return False, "La capacité doit être un nombre positif"
        
        self.dao.update_salle(salle)
        return True, "Salle mise à jour avec succès"
            
        def dellete_salle(self, code):
            return self.dao.delete_salle(code)
        
        
        def seek_salles(self , code):
            return self.dao.get_one_salle(code)
        
        def seek_all_salles(self):
            return self.dao.get_all_salles()