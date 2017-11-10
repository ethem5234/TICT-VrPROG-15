#de som van de ingevoerde getallen geven
som = 0
while True:
    getal= eval(input('Geef getal: '))
    if getal == 0:
        break
    else:
        som=som+getal
print(som)

