

class Igrac:
    def __init__(self,ime,prezime,broj,pozicija,ppg):
        self.__ime = ime
        self.__prezime = prezime
        self.__broj = broj
        self.__pozicija = pozicija
        self.__ppg = ppg


    def printaj_igraci(self):
        print(f"Ime: {self.__ime}\nPrezime: {self.__prezime}\nBroj: {self.__broj}\nPozicija: {self.__pozicija}\nPPG: {self.__ppg}\n")