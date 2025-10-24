import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import customtkinter as ctk
import tkinter.messagebox as msgbox 
import tkinter.filedialog as filedialog
import queue
from logger import infoLogger, errorLogger
import interface
from utils import formatNumber
from extractData import extractData, loadHeroesFromJson
from functools import partial
import os

DisplayMode = "Damage"
_debug = True # False to eliminate debug printing from callback functions.

def resetButton():
    # On utilise la référence enregistrée par main()
    if _w1 is None:
        msgbox.showerror("Erreur", "L’interface n’est pas encore initialisée.")
        return
    reponse = msgbox.askokcancel("Reset", "ceci entrainera la perte de données du combat actuel voulez vous continuer ?")
    if reponse:
        from calc import PlayedHeroes
        for hero in PlayedHeroes:
            hero.clear()
        PlayedHeroes.clear()
        resetListbox()
        msgbox.showinfo("Réinitialisation", "Réinitialisation effectuée")  # <<< Correction messagebox

def resetListbox(): 
    _w1.Listbox1.delete(0, 'end')


def updateHeroValue(PlayedHeroes):
    if _w1 is None:
        msgbox.showerror("Erreur", "L’interface n’est pas encore initialisée.")
        return
    displayDataOnList(PlayedHeroes)

def displayDataOnList(PlayedHeroes):
    if _w1.Listbox1.size() == 0 :
        displayDataOnListFirstTime(PlayedHeroes)
        return
    if DisplayMode == "Damage" :
        for hero in PlayedHeroes:
            _w1.Listbox1.delete(hero.DamageRank - 1)
            _w1.Listbox1.insert(hero.DamageRank - 1 , f"{hero.DamageRank} - {hero.name} [{hero.className}] : {formatNumber(hero.TotalAmountOfDamage)}")
            _w1.Listbox1.itemconfig(hero.DamageRank - 1, fg="black", bg=hero.color)
    elif DisplayMode == "Heal" :
        for hero in PlayedHeroes:
            _w1.Listbox1.delete(hero.HealRank - 1)
            _w1.Listbox1.insert(hero.HealRank - 1 , f"{hero.HealRank} - {hero.name} [{hero.className}] : {formatNumber(hero.TotalAmountOfHeal)}") 
            _w1.Listbox1.itemconfig(hero.HealRank - 1, fg="black", bg=hero.color)
    elif DisplayMode == "Shield" :
        for hero in PlayedHeroes:
            _w1.Listbox1.delete(hero.ShieldRank - 1)
            _w1.Listbox1.insert(hero.ShieldRank - 1 , f"{hero.ShieldRank} - {hero.name} [{hero.className}] : {formatNumber(hero.TotalAmountOfShield)}") 
            _w1.Listbox1.itemconfig(hero.ShieldRank - 1, fg="black", bg=hero.color)

def displayDataOnListFirstTime(PlayedHeroes):
    resetListbox()
    if DisplayMode == "Damage" :
        sorted_heroes = sorted(PlayedHeroes, key=lambda h: h.DamageRank)
        for hero in sorted_heroes:
            _w1.Listbox1.insert("end", f"{hero.DamageRank} - {hero.name} [{hero.className}] : {formatNumber(hero.TotalAmountOfDamage)}")
            _w1.Listbox1.itemconfig("end", fg="black", bg=hero.color)
    elif DisplayMode == "Heal" :
        sorted_heroes = sorted(PlayedHeroes, key=lambda h: h.HealRank)
        for hero in sorted_heroes:
            _w1.Listbox1.insert("end", f"{hero.HealRank} - {hero.name} [{hero.className}] : {formatNumber(hero.TotalAmountOfHeal)}")
            _w1.Listbox1.itemconfig("end", fg="black", bg=hero.color)
    elif DisplayMode == "Shield" :
        sorted_heroes = sorted(PlayedHeroes, key=lambda h: h.ShieldRank)
        for hero in sorted_heroes:
            _w1.Listbox1.insert("end", f"{hero.ShieldRank} - {hero.name} [{hero.className}] : {formatNumber(hero.TotalAmountOfShield)}")
            _w1.Listbox1.itemconfig("end", fg="black", bg=hero.color)
def switchButton(mode):
    print(f"mode = {mode}")
    if _w1 is None:
        msgbox.showerror("Erreur", "L’interface n’est pas encore initialisée.")
        return
    _w1.Listbox1.delete(0, 'end')
    infoLogger.info(f"{mode} button clicked")
    global DisplayMode
    DisplayMode = mode
    from calc import PlayedHeroes
    displayDataOnListFirstTime(PlayedHeroes)

def enforce_topmost(root):
    root.attributes('-topmost', True)
    root.lift()

def on_focus_out(event):
    enforce_topmost(event.widget)

def extractdata():
    from calc import PlayedHeroes
    outputFileName = extractData(PlayedHeroes)
    msgbox.showinfo("Export terminé", f"Export terminé : {outputFileName} ({len(PlayedHeroes)} héros exportés)")


def importdata():
    from calc import PlayedHeroes
    file = None
    reponse = msgbox.askyesno(
        title="Confirmation",
        message="L'importation de données va effacer les données actuelles. Voulez-vous vraiment effectuer cette action ?"
    )
    if reponse:
        from calc import PlayedHeroes
        for hero in PlayedHeroes:
            hero.clear()
        PlayedHeroes.clear()
        resetListbox()
        file = chooseFileForImport()
    if file == None :
        return
    PlayedHeroes = loadHeroesFromJson(file, PlayedHeroes)
    displayDataOnListFirstTime(PlayedHeroes)

def chooseFileForImport():
    file = filedialog.askopenfilename(
        title="Choisissez un fichier JSON",
        filetypes=[("Fichiers JSON", "*.json"), ("Tous les fichiers", "*.*")]
    )
    if file:  # Si un fichier a été sélectionné
        msgbox.showinfo("Fichier sélectionné", f"Vous avez choisi :\n{file}")
        print("Fichier choisi :", file)
        return file
    else:
        msgbox.showwarning("Aucun fichier", "Aucun fichier n’a été sélectionné.")
        return None
def open_settings(choice):
    print(f"{choice} MENU button clicked")
    if choice == "Reset" :
        resetButton()
    elif choice == "History" :
        ShowHistory()
    elif choice == "Import Data" :
        importdata()
    _w1.Parametres.configure(variable=ctk.StringVar(value="Options"))
    print("sortis de open_settings")

def ShowHistory():
    from calc import PlayedHeroes
    window = ctk.CTkToplevel(root)
    window.title("History")
    window.attributes('-topmost', True)
    window.attributes("-alpha", 0.8)
    window.lift()
    #window.geometry("600x400")

    scrolableFrame = ctk.CTkScrollableFrame(window, label_text="Rapport History")
    scrolableFrame.pack(fill="both", expand=True, padx=10, pady=10)
    for i, nom_fichier in enumerate(os.listdir("Rapport")):
        chemin_complet = os.path.join("Rapport", nom_fichier)
        #print(chemin_complet)
        if os.path.isfile(chemin_complet):
            label = ctk.CTkLabel(scrolableFrame, text=nom_fichier)
            label.grid(row=i, column=0, sticky="w", padx=10, pady=5)

            bouton = ctk.CTkButton(
                scrolableFrame,
                text="Ouvrir",
                width=40,
                height=10,
                command=lambda p=chemin_complet: [loadHeroesFromJson(p, PlayedHeroes), displayDataOnListFirstTime(PlayedHeroes)]
            )
            bouton.grid(row=i, column=1, padx=10, pady=5, sticky="e")
            #print(chemin_complet)
            #print(nom_fichier)
    #PlayedHeroes = loadHeroesFromJson(chemin_complet, PlayedHeroes)
    #displayDataOnListFirstTime(PlayedHeroes)

def main(*args):
    global root
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    root.attributes("-alpha", 0.8)

    root.attributes('-topmost', True)
    root.lift()
    #enforce_topmost(root)
    #root.bind('<FocusOut>', on_focus_out)   # lorsqu'on clique ailleurs
    #root.bind('<Map>', lambda e: enforce_topmost(root))
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = interface.Toplevel1(_top1)
    # <<< AJOUT — on enregistre la référence de l’interface ici
    interface._w1 = _w1

    root.mainloop()

if __name__ == '__main__':
    main()