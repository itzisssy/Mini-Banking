# Einzahlen, Abheben, Kontostand abfragen

Kontostand = [0]


print("a) Einzahlen\nb) Auszahlen\nc) Kontostand abfrage:")
Eingabe = input("Wählen Sie eine von den drei Optionen: ")

if Eingabe == "a":
    print("Wie viel wohlen sie einzahlen?")
    Einzahlen = float(input("Summe: "))
    Kontostand[0] += Einzahlen
    print(f"Auf dein Konto ist jetz {Kontostand[0]} Euro")
elif Eingabe == "b":
    print(f"Sie haben {Kontostand[0]} Wie viel wollen sie auszahlen?")
    Auszahlen = float(input("Summe: "))
    Kontostand[0] -= Auszahlen
    print(f"Du hast {Auszahlen} Euro ausgezahlt.")
elif Eingabe == "c":
    print(f"Du hast momentan {Kontostand[0]} Euro auf deinem Konto.")
else:
    print("Bitte wählen eine Option der drei aus.")