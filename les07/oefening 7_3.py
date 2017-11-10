#tellen met behulp van dictenary
zin= 'all animals are equel but some animals are more equel than other'
#woordenteller
# woord = key
#value = woordenteller[woord]

# de zin declareren
#woorden nodig => zin splitsen op spatie
# initialiseer woordenteller op een dictinairy
# lijst doorlopen a. als woord voorkomt, teller met 1 ophogen b. anders woord teovoegen aan dictenairy en teller op 1 zetten
woorden = zin.split()
woordenteller= {}
for woord in woorden:
    if woord in woordenteller.keys():
        # teller met 1 ophogen
        woordenteller[woord] += 1
   #
    else:
        woordenteller[woord] = 1
print(woordenteller)
#format methode gebruiken om hem netjes onderelkaar te krijgen
for woord in woordenteller:
    print('{:8} komt {:1} keer voor.'.format(woord, woordenteller[woord]))
