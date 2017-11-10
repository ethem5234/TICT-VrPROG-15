getallenrij= [2,4,6,8,10,10,9,7]
zoekgetal= eval(input('voer een getal in: '))
gevonden= False
for getal in getallenrij:
    if getal == zoekgetal:
        gevonden = True
else: print('Getal niet gevonden')
print(gevonden)