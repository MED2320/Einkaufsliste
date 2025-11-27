# Einkaufsliste-Programm
# Muhammed Emin Dursun
# 26-11-2025


# Funktion: Menü anzeigen
def menue():
    print("\n--- Einkaufsliste ---")
    print("1) Produkt hinzufügen")
    print("2) Liste anzeigen")
    print("3) Produkt löschen")
    print("4) Beenden")

# Funktion: Produkt hinzufügen
def produkt_hinzufuegen(liste):
    produkt = input("Produkt eingeben: ")

    # Leere Eingaben verhindern
    if produkt == "":
        print("Du musst etwas eingeben.")
        return

    liste.append(produkt)
    print("Produkt hinzugefügt.")

# Funktion: Liste anzeigen
def liste_anzeigen(liste):
    if len(liste) == 0:
        print("Die Einkaufsliste ist leer.")
    else:
        print("\n--- Deine Einkaufsliste ---")
        # Produkte mit Nummer anzeigen
        for i in range(len(liste)):
            print(str(i + 1) + ") " + liste[i])

# Funktion: Produkt löschen
def produkt_loeschen(liste):
    if len(liste) == 0:
        print("Liste ist leer. Nichts zu löschen.")
        return

    liste_anzeigen(liste)

    nummer = input("Nummer des Produkts zum Löschen: ")

    # Prüfen, ob Zahl eingegeben wurde
    if not nummer.isdigit():
        print("Bitte eine gültige Zahl eingeben.")
        return

    nummer = int(nummer)

    if nummer < 1 or nummer > len(liste):
        print("Ungültige Nummer.")
        return

    liste.pop(nummer - 1)
    print("Produkt gelöscht.")

# Hauptfunktion (Programmstart)
def main():
    einkaufsliste = []
    laufend = True

    while laufend:
        menue()
        auswahl = input("Option wählen: ")

        if auswahl == "1":
            produkt_hinzufuegen(einkaufsliste)
        elif auswahl == "2":
            liste_anzeigen(einkaufsliste)
        elif auswahl == "3":
            produkt_loeschen(einkaufsliste)
        elif auswahl == "4":
            print("Programm beendet.")
            laufend = False
        else:
            print("Ungültige Eingabe.")

# Programm starten
main()