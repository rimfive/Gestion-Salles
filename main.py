
from models.salle import salle
from Data.dao_salles import dataSalles

# Créer une instance du DAO
dao = dataSalles()

try:
    # Créer la table si elle n'existe pas
    dao.create_table()
    print("Table créée ou déjà existante")

    # test insert
    s1 = salle("S001", "Salle de conférence", "Conférence", 100)
    dao.insert_salle(s1)
    print("Insertion réussie")

    # test update
    s1.libelle = "Salle de réunion"
    dao.update_salle(s1)
    print("Mise à jour réussie")

    # test get one
    salle_recup = dao.get_one_salle("S001")
    if salle_recup:
        salle_recup.afficher()
    else:
        print("Salle non trouvée")

    # test get all
    salles = dao.get_all_salles()
    print(f"Nombre de salles: {len(salles)}")

except Exception as e:
    print(f"Erreur: {e}")
