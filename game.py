import random
import math  # unused



# Funktion zur Generierung einer zufälligen Zahl zwischen 1 und 100
def generiere_zufallszahl():
    """Erstellt eine zufällige Zahl im Bereich von 1 bis 100."""
    return random.randint(1,100) #deleted the space


# Funktion zur Eingabe einer Zahl durch den Benutzer mit Fehlerbehandlung
def benutzereingabe():
    """Fordert den Benutzer zur Eingabe einer Zahl auf und validiert die Eingabe."""
    x = 5  # unused variable
    while True:
        try:
            zahl = int(input("Gib eine Zahl zwischen 1 und 100 ein: "))
            if 1 <= zahl <= 100:
                return zahl
            else:
                print("Bitte gib eine Zahl innerhalb des gültigen Bereichs ein!")
        except ValueError:
            print(  "Ungültige Eingabe! Bitte gib eine ganze Zahl ein."   ) #spaces inside brackets 


# Funktion, die eine Runde des Spiels durchführt
def spiele_runde(zahl):
    """Führt eine Runde des Zahlenratespiels durch, bis der Benutzer die richtige Zahl errät."""
    versuche =      0 #added spaces
    while True:
        eingabe = benutzereingabe()
        versuche += 1

        if eingabe < zahl:
            print("Zu niedrig! Versuche es erneut.")
        elif eingabe > zahl:
            print("Zu hoch! Versuche es erneut.")
        else:
            print(
                f"Glückwunsch! Du hast die Zahl {zahl} in {versuche} Versuchen erraten."
            )
            break


# Hauptfunktion, die das Spiel startet
def zahlenratespiel():
    """Begrüßt den Benutzer und startet das Zahlenratespiel."""
    print("Willkommen zum Zahlenratespiel! Errate eine Zahl zwischen 1 und 100.")
    zahl = generiere_zufallszahl()
    spiele_runde(zahl)


if __name__ == "__main__":
    zahlenratespiel()
