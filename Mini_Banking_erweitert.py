# # Einzahlen, Abheben, Kontostand abfragen, Programm Beenden, Speicherung des Kontostands

try:
    datei = open("kontostand.txt", "r")
    Kontostand = [float(datei.read())] 
except:
    Kontostand = [0] 

while True:
    print("\n--- Mini-Banking ---")
    print("a) Einzahlen")
    print("b) Auszahlen")
    print("c) Kontostand abfragen")
    print("d) Beenden")
    Auswahl = input("Wählen Sie eine Option: ")

    if Auswahl == "a":
        Betrag = float(input("Wie viel wollen Sie einzahlen? "))
        Kontostand[0] += Betrag
        print(f"Auf dein Konto ist jetzt {Kontostand[0]} Euro")
    elif Auswahl == "b":
        Betrag = float(input(f"Du hast {Kontostand[0]} Euro. Wie viel willst du abheben? "))
        if Betrag <= Kontostand[0]:
            Kontostand[0] -= Betrag
            print(f"Neuer Kontostand: {Kontostand[0]} Euro")
        else:
            print("Fehler: Nicht genug Geld auf dem Konto!")
    elif Auswahl == "c":
        print(f"Dein Kontostand beträgt: {Kontostand[0]} Euro")
    elif Auswahl == "d":
        # Kontostand speichern bevor Programm endet
        datei = open("kontostand.txt", "w")
        datei.write(str(Kontostand[0]))
        datei.close()
        print("Programm beendet. Kontostand gespeichert.")
        break
    else:
        print("Ungültige Option. Bitte a, b, c oder d wählen.")
