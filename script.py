#!/usr/bin/env python3

from typing import List, Tuple

# Aufgabe: Erstellen Sie eine Klasse 'BankAccount', die ein einfaches Bankkonto repräsentiert.
class BankAccount:
# 1. Die Klasse soll die folgenden Attribute (Member-Variablen) haben:
#    - Inhaber: Der Name des Kontoinhabers (öffentlich).
#    - Kontonummer: Eine eindeutige Kontonummer (öffentlich).
#    - __kontostand: Der aktuelle Kontostand (nicht öffentlich).
    def __init__(self, inhaber:str, kontonummer:int, startkontostand:float):
        self.inhaber=inhaber
        self.kontonummer=kontonummer
        self.__kontostand=startkontostand
        self._transaktionen: List[Tuple[str, float]] = []       

# 2. Implementieren Sie die folgenden Methoden:
#    - __init__: Initialisiert den Kontoinhaber, die Kontonummer und den anfänglichen Kontostand.
#    - einzahlen: Erhöht den Kontostand um einen bestimmten Betrag.
#    - abheben: Verringert den Kontostand um einen bestimmten Betrag, wenn genügend Guthaben vorhanden ist.
#    - get_kontostand: Gibt den aktuellen Kontostand zurück.
    def einzahlen(self, einzahl_betrag:float)->float:
        self.__kontostand += einzahl_betrag
        print("Es wurden " + str(einzahl_betrag) + " EUR eingezahlt" )
        self._transaktionen.append(("Einzahlung", einzahl_betrag))
        return self.__kontostand


    def abheben(self, abheb_betrag:float)->float:
        self.__kontostand -= abheb_betrag
        print("Es wurden " + str(abheb_betrag) + " EUR abgehoben" )
        self._transaktionen.append(("Auszahlung", abheb_betrag))
        return self.__kontostand

    def get_kontostand(self)->float:
        return self.__kontostand
# 3. Implementieren Sie außerdem eine Methode __str__, die eine benutzerfreundliche Darstellung des Kontos zurückgibt.
    def __str__(self)->str:
        return (
            f"Konto von {self.inhaber}\n"
            f"Kontonummer: {self.kontonummer}\n"
            f"Aktueller Kontostand: {self.__kontostand:.2f} EUR"
        )
  
    def get_transaktionen(self) -> List[Tuple[str, float]]:
        """Gibt eine Liste aller Transaktionen zurück."""
        return self._transaktionen
# Optional:
# - Erstellen Sie eine Methode, die Transaktionen protokolliert und eine Liste von Ein- und Auszahlungen ausgibt.

mein_account=BankAccount("Julian",71011,50)
print(mein_account)
mein_account.einzahlen(30)
print(mein_account)
mein_account.abheben(10)
print(mein_account)

dein_account=BankAccount("Bibi",71012,500)
print(dein_account)
dein_account.einzahlen(30)
print(dein_account)

print(mein_account.List)