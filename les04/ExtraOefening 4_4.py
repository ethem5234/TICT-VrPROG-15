def eindbedrag(bedrag):
    bedrag = bedrag + rente * bedrag / 100
    return bedrag

bedrag= eval(input('Geef een bedrag: '))
rente= eval(input('geef een rentepercentage: '))
print(eindbedrag(bedrag))