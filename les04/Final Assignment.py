def standaardtarief(KM):
        KM=eval(input('Voer hier uw afstand in kilomers in:'))
        if KM <= 50:
            return KM*0.80
        elif KM> 50:
            return 15+(KM*0.60)
        else:
            return 0

def ritprijs(leeftijd, weekendrit, KM):
    weekend=True
    week=False
    weekendrit=input('vind de rit plaats in de week of weekend?: ')
    leeftijd=eval(input('Wat is uw leeftijd?: '))
    standaardtarief(KM)
    if weekendrit==False and leeftijd <=12 or leeftijd >= 65:
        return weekendrit * 0.75
    if weekendrit==True and leeftijd <=12 or leeftijd >= 65:
        return weekendrit * 0.70
    if weekendrit==False and leeftijd >12 or leeftijd < 65:
        return weekendrit
    if weekendrit==True and leeftijd >12 or leeftijd < 65:
        return  weekendrit * 0.60
ritprijs(12,'week',20)
