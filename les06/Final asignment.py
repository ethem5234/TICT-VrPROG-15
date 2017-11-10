def toon_aantalkluizen_vrij():
    infile=open('kluizen.txt','r')
    kluizendata=infile.readlines()
    infile.close()

    aantalkluizen=len(kluizendata)
    aantalvrij=12-aantalkluizen
    print('Er zijn '+str(aantalvrij)+' kluizen vrij')
def nieuw_kluis():
    print('2')
def kuis_openen():
    infile= open('kluizen.txt','r')
    kluizendata=infile.readlines()
    infile.close()

    stringnummer=input('Geef een nummer: ')
    ww= input('geef je wachtwoord: ')

    gegevens_correct=False

    for regel in kluizendata:
        gegevens_van_een_kluis=regel.split(';')
        string_kluisnummer=gegevens_van_een_kluis[0]
        kluiscode=gegevens_van_een_kluis[1].strip()

        if string_kluisnummer == stringnummer and kluiscode == ww:
            gegevens_correct=True
    if gegevens_correct == True:
        print('kluis is open')
    else:
        print('Je gegevens kloppen niet')

def aantal_kluizen_vrij():
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readline()
    infile.close()
aantalkluizen=len(kluizendata)
aantalvrij=12*aantalkluizen
gegevenscorrect=False
if stringnummer == stringkluizennummer and kluiscode==code:
    gegevenscorrect=True

def kluis_openen():
    infile= open()
    kluizendata= infile.readlines()
    infile.close()
stringnummer= input('wat is je nummer: ')
code = input('wat is je code: ')
for regel in kuizendata:
    gegevensvan1kluis= regel.split(',')
    stringnummer=gegevensvan1kluis[0]
    kluiscode= gegevensvan1kluis[1]
if gegevenscorrect:
    print('correct')
else:
    print('niet correct')

print('1: Ik wil weten hoeveel kluisen er nog vrij zijn')
print('2: Ik wil een nieuwe kluis')
print('3: Ik wil iets uit mijn kluis halen')
print('4: Ik geef mijn kluis terug')
print('5: ik wil stoppen')
keuze =eval(input('Maak een keuze: '))