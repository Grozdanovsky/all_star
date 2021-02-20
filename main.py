from igrac import *



i1 = Igrac("Bradley","Beal","3","SG",32.8)

i2 = Igrac("Stephen","Curry","30","PG",29.9)

i3 = Igrac("Kevin","Durant","7","PF",29)

i4 = Igrac("Kyrie","Irving","11","PG",27)

i5 = Igrac("LeBron","James","23","SF",26)


lista_igraci = [i1,i2,i3,i4,i5]

for item in lista_igraci:
    item.printaj_igraci()

