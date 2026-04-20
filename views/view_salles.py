import os
import sys

if sys.platform == "win32":
    base_prefix = getattr(sys, "base_prefix", sys.prefix)
    tcl_dir = os.path.join(base_prefix, "tcl", "tcl8.6")
    tk_dir = os.path.join(base_prefix, "tcl", "tk8.6")
    if os.path.isdir(tcl_dir):
        os.environ["TCL_LIBRARY"] = tcl_dir
    if os.path.isdir(tk_dir):
        os.environ["TK_LIBRARY"] = tk_dir

import customtkinter as ctk
from services.services_salle import ServiceSalle
from models.salle import salle
from tkinter import ttk

class ViewSalles(ctk.CTk):

    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        self.title("Gestion des salles")
        self.geometry("750x550")

        self.service = ServiceSalle()

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(padx=20, pady=20, fill="x")

        self.entry_Code = ctk.CTkEntry(self.frame, placeholder_text="Code")
        self.entry_Code.pack(pady=5, fill="x")

        self.entry_Libelle = ctk.CTkEntry(self.frame, placeholder_text="Libellé")
        self.entry_Libelle.pack(pady=5, fill="x")

        self.entry_Type = ctk.CTkEntry(self.frame, placeholder_text="Type de salle")
        self.entry_Type.pack(pady=5, fill="x")

        self.entry_Capacite = ctk.CTkEntry(self.frame, placeholder_text="Capacité")
        self.entry_Capacite.pack(pady=5, fill="x")

        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(padx=20, pady=10, fill="x")

        ctk.CTkButton(self.button_frame, text="Ajouter", command=self.add_salle).pack(side="left", padx=5)
        ctk.CTkButton(self.button_frame, text="Modifier", command=self.update_salle).pack(side="left", padx=5)
        ctk.CTkButton(self.button_frame, text="Supprimer", command=self.delete_salle).pack(side="left", padx=5)
        ctk.CTkButton(self.button_frame, text="Rechercher", command=self.search_salle).pack(side="left", padx=5)

        self.tree_frame = ctk.CTkFrame(self)
        self.tree_frame.pack(padx=20, pady=10, fill="both", expand=True)

        self.tree = ttk.Treeview(self.tree_frame, columns=("Code", "Libellé", "Type", "Capacité"), show="headings", height=10)
        self.tree.heading("Code", text="Code")
        self.tree.heading("Libellé", text="Libellé")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Capacité", text="Capacité")
        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<ButtonRelease-1>", self.on_tree_select)

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
            self.clear_fields()

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
            self.clear_fields()

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
        for s in self.service.get_all_salles():
            self.tree.insert("", "end", values=(s.code, s.libelle, s.type_salle, s.capacite))

    def clear_fields(self):
        self.entry_Code.delete(0, "end")
        self.entry_Libelle.delete(0, "end")
        self.entry_Type.delete(0, "end")
        self.entry_Capacite.delete(0, "end")

    def on_tree_select(self, event):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            values = item['values']
            self.entry_Code.delete(0, "end")
            self.entry_Code.insert(0, str(values[0]))
            self.entry_Libelle.delete(0, "end")
            self.entry_Libelle.insert(0, str(values[1]))
            self.entry_Type.delete(0, "end")
            self.entry_Type.insert(0, str(values[2]))
            self.entry_Capacite.delete(0, "end")
            self.entry_Capacite.insert(0, str(values[3]))

        else:
            self.clear_fields()


if __name__ == '__main__':
    app = ViewSalles()
    app.mainloop()
    


