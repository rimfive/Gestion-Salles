"""""""""""
from models.salle import salle
from Data.dao_salles import dataSalles


dao = dataSalles()

try:
    
    dao.create_table()
    print("Table créée ou déjà existante")

   
    s1 = salle("S001", "Salle de conférence", "Conférence", 100)
    dao.insert_salle(s1)
    print("Insertion réussie")


    s1.libelle = "Salle de réunion"
    dao.update_salle(s1)
    print("Mise à jour réussie")

    
    salle_recup = dao.get_one_salle("S001")
    if salle_recup:
        salle_recup.afficher()
    else:
        print("Salle non trouvée")

   
    salles = dao.get_all_salles()
    print(f"Nombre de salles: {len(salles)}")

except Exception as e:
    print(f"Erreur: {e}")
"""""""""

from services.services_salle import ServiceSalle
from models.salle import salle

service = ServiceSalle()

# Nettoyer les données de test précédentes
service.delete_salle("E3")

s = salle("E3", "Salle Scientifique", "Classe", 16)

ok, msg = service.add_salle(s)
print(msg)

liste = service.get_salles()
for salles in liste:
    salles.afficher()
