leeftijd= eval(input('Wat is je leeftijd: '))

paspoort= input('Ben je in het bezit van een nederlandse paspoort: ')=='ja'
if leeftijd >= 18 and paspoort==True:
    print('Gefeliciteerd, je mag stemmen!')