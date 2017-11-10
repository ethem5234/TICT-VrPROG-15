def eindbedrag(bedrag,rente):
    bedrag = bedrag+rente*bedrag/100
    print(bedrag)

bedrag= eval(input('Geef een bedrag: '))
rente= eval(input('geef een rentepercentage: '))
eindbedrag(bedrag,rente)
