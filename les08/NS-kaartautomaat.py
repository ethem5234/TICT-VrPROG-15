stations = ['Schagen', 'Heerhugowaard','Alkmaar','Castricum','Zaandam','Amsterdam Sloterdijk','Amsterdam Centraal','Amsterdam Amstel','Utrecht Centraal','’s-Hertogenbosch','Eindhoven','Weert','Roermond','Sittard','Maastricht']


def inlezen_beginstation(stations):
    beginstation = input('Voer hier uw vertrekpunt in: ')

    while  beginstation not in stations:
        beginstation = input('Voer hier een nieuw vertekpunt in: ')
    return beginstation

def inlezen_eindstation(stations, beginstation):
    eindstation = input('Voer hier uw bestemming in: ')

    while eindstation not in stations:
        eindstation= input('Voer hier uw nieuwe bestemming in: ')
    while stations.index(beginstation)>=stations.index(eindstation):
        eindstation= input('Geef een nieuwe bestemming aan: ')
    return eindstation

def omroepen_reis(stations, beginstation, eindstation):
    NummerB=stations.index(beginstation)+1
    NummerE=stations.index(eindstation)+1
    afstand= NummerE-NummerB
    print('\nHet beginstation {} is het {}e station in het traject.'.format(beginstation,NummerB))
    print('Het eindstation {} is het {}e station in het traject.'.format(eindstation,NummerE))
    print('De afstand bedraagt {} station(s).',format(afstand))
    print('De prijs van de kaartjes is '+str(((stations.index(eindstation)-stations.index(beginstation))*5))+' euro.')
    print('Je stapt in de trein in: {}'.format(beginstation))
    for i in range(NummerB, NummerE-1):
        print('-'+stations[i])
    print('Je stapt uit in: {}'.format(eindstation))


beginstation= inlezen_beginstation(stations)
eindstation= inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)