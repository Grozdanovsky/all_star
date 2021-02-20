

class Igrac:
    def __init__(self,ime,prezime,broj,pozicija,ppg):
        self.__ime = ime
        self.__prezime = prezime
        self.__broj = broj
        self.__pozicija = pozicija
        self.__ppg = ppg

    def getPPG(self):
        return self.__ppg