from igrac import *
import random
from team import *



i1 = Igrac("Bradley","Beal","3","SG",32.8)

i2 = Igrac("Stephen","Curry","30","PG",29.9)

i3 = Igrac("Kevin","Durant","7","PF",29)

i4 = Igrac("Kyrie","Irving","11","PG",27)

i5 = Igrac("LeBron","James","23","SF",26)

i6 = Igrac("Luka","Doncic","77","SF",29)

i7 = Igrac("Trae","Young","11","PG",27)

i8 = Igrac("Kawhi","Leonard","2","SG",26)

i9 = Igrac("Giannis","Antetokounmpo","34","PF",28)

i10 = Igrac("Anthony","Davis","3","C",26.1)


def add_players(lista_na_igraci):

    random.shuffle(lista_na_igraci)
    tim1 = []
    tim2 = []
    brojac = 1
    for item in lista_na_igraci:
        if brojac %2 == 0:
            tim1.append(item)
            brojac += 1
        else:
            tim2.append(item)
            brojac += 1

    return [tim1,tim2]


### MAIN ###

lista_igraci = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10]


timovi = add_players(lista_igraci)

t1 = Team("West",timovi[0])

t2 = Team("East",timovi[1])

t1.printaj_tim()
t2.printaj_tim()

t1.printPlayersByPPG()

t2.printPlayersByPPG()



