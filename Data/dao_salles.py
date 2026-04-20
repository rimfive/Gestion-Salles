import mysql.connector
import json
from models.salle import salle

class dataSalles:
    def get_connexion(self):
        with open('Data/config.json', 'r') as f:
            config = json.load(f)
        
        conn = mysql.connector.connect(
            host=config['host'],
            user=config['user'],
            password=config['password'],
            database=config['database']
        )

        return conn
    
    def create_table(self):
        conn = self.get_connexion()
        cursor = conn.cursor()

        query = """
        CREATE TABLE IF NOT EXISTS salles (
            code VARCHAR(10) PRIMARY KEY,
            libelle VARCHAR(100) NOT NULL,
            type_salle VARCHAR(50) NOT NULL,
            capacite INT NOT NULL
        )
        """
        cursor.execute(query)
        conn.commit()

        cursor.close()
        conn.close()
    
    def insert_salle(self, salle):
        conn = self.get_connexion()
        cursor = conn.cursor()

        query = "INSERT INTO salles (code, libelle, type_salle, capacite) VALUES (%s, %s, %s, %s)"
        values = (salle.code, salle.libelle, salle.type_salle, salle.capacite)

        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

    def update_salle(self, salle):
        conn = self.get_connexion()
        cursor = conn.cursor()

        query = "UPDATE salles SET libelle = %s, type_salle = %s, capacite = %s WHERE code = %s"
        values = (salle.libelle, salle.type_salle, salle.capacite, salle.code)

        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()


    def delete_salle(self, code):
        conn = self.get_connexion()
        cursor = conn.cursor()

        query = "DELETE FROM salles WHERE code = %s"
        values = (code,)
        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()
