import customtkinter as ctk
from services.services_salle import ServiceSalle
from models.salle import salle
from tkinter import ttk

class ViewSalles(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("600x500")

        self.service = ServiceSalle()

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=10)

        self.entry_Code = ctk.CTkEntry(self.frame, placeholder_text="Code")
        self.entry_Code.pack(pady=5)

        self.entry_Libelle = ctk.CTkEntry(self.frame, placeholder_text="Libellé")
        self.entry_Libelle.pack(pady=5)

        self.entry_Type = ctk.CTkEntry(self.frame, placeholder_text="Type de salle")
        self.entry_Type.pack(pady=5)

        self.entry_Capacite = ctk.CTkEntry(self.frame, placeholder_text="Capacité")
        self.entry_Capacite.pack(pady=5)

    
        self.fram_btn = ctk.CTkFrame(self)
        self.fram_btn.pack(pady=10)

        ctk.CTkButton(self.fram_btn, text="Ajouter", command=self.add_salle).pack(side="left", padx=5)
        ctk.CTkButton(self.fram_btn, text="Modifier", command=self.update_salle).pack(side="left", padx=5)
        ctk.CTkButton(self.fram_btn, text="Supprimer", command=self.delete_salle).pack(side="left", padx=5)
        ctk.CTkButton(self.fram_btn, text="Rechercher", command=self.search_salle).pack(side="left", padx=5)

        self.tree = ttk.Treeview(self, columns=("Code", "Libellé", "Type", "Capacité"), show="headings")
        self.tree.heading("Code", text="Code")
        self.tree.heading("Libellé", text="Libellé")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Capacité", text="Capacité")
        self.tree.pack(fill="both", expand=True)

        self.liste_salles()

    def add_salle(self):
        try:
            capacite = int(self.entry_Capacite.get())
        except ValueError:
            print("Capacité doit être un nombre entier")
            return

        salle_obj = salle(
            self.entry_Code.get(),
            self.entry_Libelle.get(),
            self.entry_Type.get(),
            capacite
        )

        ok, msg = self.service.add_salle(salle_obj)
        print(msg)
        if ok:
            self.liste_salles()
          
            self.entry_Code.delete(0, "end")
            self.entry_Libelle.delete(0, "end")
            self.entry_Type.delete(0, "end")
            self.entry_Capacite.delete(0, "end")

    def update_salle(self):
        try:
            capacite = int(self.entry_Capacite.get())
        except ValueError:
            print("Capacité doit être un nombre entier")
            return

        salle_obj = salle(
            self.entry_Code.get(),
            self.entry_Libelle.get(),
            self.entry_Type.get(),
            capacite
        )

        ok, msg = self.service.update_salle(salle_obj)
        print(msg)
        if ok:
            self.liste_salles()

    def delete_salle(self):
        code = self.entry_Code.get()
        ok, msg = self.service.delete_salle(code)
        print(msg)
        if ok:
            self.liste_salles()
            

            self.entry_Code.delete(0, "end")
            self.entry_Libelle.delete(0, "end")
            self.entry_Type.delete(0, "end")
            self.entry_Capacite.delete(0, "end")

    def search_salle(self):
        code = self.entry_Code.get()
        salle_obj = self.service.get_salle(code)
        if salle_obj:
            self.entry_Libelle.delete(0, "end")
            self.entry_Libelle.insert(0, salle_obj.libelle)

            self.entry_Type.delete(0, "end")
            self.entry_Type.insert(0, salle_obj.type_salle)

            self.entry_Capacite.delete(0, "end")
            self.entry_Capacite.insert(0, str(salle_obj.capacite))
        else:
            print("Salle non trouvée")

    def liste_salles(self):
        self.tree.delete(*self.tree.get_children())

        salles = self.service.get_salles()
        for s in salles:
            self.tree.insert("", "end", values=(s.code, s.libelle, s.type_salle, s.capacite))

if __name__ == '__main__':
    app = ViewSalles()
    app.mainloop()
            