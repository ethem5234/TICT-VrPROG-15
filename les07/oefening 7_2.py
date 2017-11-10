week = {'ma': 'maandag', 'di': 'dindag', 'wo': 'woensdag', 'do':'donderdag', 'vr': 'vrijdag'}
#voor de dubbele punt:key
# na de dubbelepunt value
#samen = item

print(week)
print('ma' in week)
# print de value
print(week ['ma'])
#veranderen van value
week['di']='dinsdag'
print(week)
# teovoegen van item
week['za']= 'zaterdag'
print(week)
# keys afdrukken
for afkorting in week.keys():
    print(afkorting)
# .keys mag je weglaten
# values afdrukken
for langenaam in week.values():
    print(langenaam)
# items afdrukken
for beide in week.items():
    print(beide)
#andere (duidelijkere) manier voor items is:
for afkorting in week.keys():
    print(afkorting, week[afkorting])
#met format methode
for afkorting in week:
    print('Afkorting: {}, lange naam: {}'.format(afkorting, week[afkorting]))
#ook hier mag je .keys() weglaten