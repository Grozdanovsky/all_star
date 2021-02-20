
class Team:
    def __init__(self,ime,lista_igraci):
        self.__ime = ime
        self.__lista_igraci = lista_igraci

    def printaj_igraci(self):
        for item in self.__lista_igraci:
            item.printaj_igraci()

    def printaj_tim(self):
        print(f"{self.__ime}\n\nPlayers:\n")
        self.printaj_igraci()


    def printPlayersByPPG(self):
        sortedLista =  sorted(self.__lista_igraci,key=lambda x: x.getPPG(),reverse = True)
        for item in sortedLista:
           item.printaj_igraci()

