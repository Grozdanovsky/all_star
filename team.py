
class Team:
    def __init__(self,ime,lista_igraci):
        self.__ime = ime
        self.__lista_igraci = lista_igraci


    def printaj_tim(self):
        print(f"{self.__ime}\n Players:\n{self.__lista_igraci}")


    # print funckija za timot

    # print funckija za igraci vo timot

    #sort funkcija i da printa

    def printPlayersByPPG(self):
        sortedLista =  sorted(self.__lista_igraci,key=lambda x: x.getPPG(),reverse = True)
        for item in sortedLista:
            print(item.printaj_igraci())