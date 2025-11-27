# Einkaufsliste-Programm mit GUI
# Muhammed Emin Dursun
# 27-11-2025


import tkinter as tk
from tkinter import messagebox

# -----------------------------

def produkt_hinzufuegen():
    produkt = eingabe_feld.get()

    if produkt.strip() == "":
        messagebox.showwarning("Fehler", "Bitte ein Produkt eingeben.")
        return

    einkaufsliste.append(produkt)
    listbox.insert(tk.END, produkt)
    eingabe_feld.delete(0, tk.END)

def produkt_loeschen():
    auswahl = listbox.curselection()

    if not auswahl:
        messagebox.showinfo("Info", "Bitte ein Produkt auswählen.")
        return

    index = auswahl[0]
    produkt = einkaufsliste[index]

    loeschen = messagebox.askyesno("Löschen", f"'{produkt}' wirklich löschen?")
    if loeschen:
        listbox.delete(index)
        einkaufsliste.pop(index)

def liste_leeren():
    if not einkaufsliste:
        messagebox.showinfo("Info", "Liste ist bereits leer.")
        return

    bestaetigung = messagebox.askyesno("Liste leeren", "Liste wirklich leeren?")
    if bestaetigung:
        einkaufsliste.clear()
        listbox.delete(0, tk.END)

def beenden():
    fenster.destroy()



# -----------------------------
# Hauptfenster
# -----------------------------
fenster = tk.Tk()
fenster.title("Einkaufsliste")
fenster.geometry("300x400")

einkaufsliste = []

# Eingabefeld
eingabe_feld = tk.Entry(fenster, width=25)
eingabe_feld.pack(pady=10)

# Buttons
btn_hinzufuegen = tk.Button(fenster, text="Produkt hinzufügen", command=produkt_hinzufuegen)
btn_hinzufuegen.pack(pady=5)
eingabe_feld.bind("<Return>", lambda event: produkt_hinzufuegen())

btn_loeschen = tk.Button(fenster, text="Produkt löschen", command=produkt_loeschen)
btn_loeschen.pack(pady=5)

btn_leeren = tk.Button(fenster, text="Liste leeren", command=liste_leeren)
btn_leeren.pack(pady=5)

# Listbox zur Anzeige der Einkaufsliste
listbox = tk.Listbox(fenster, width=30, height=10)
listbox.pack(pady=10)

# Beenden-Button
btn_beenden = tk.Button(fenster, text="Beenden", command=beenden)
btn_beenden.pack(pady=5)

# -----------------------------
# Programm Start
# -----------------------------
fenster.mainloop()
