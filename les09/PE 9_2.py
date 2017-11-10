import csv
with open('inloggers.csv','w',newline='') as myCSVFile:
    writer=csv.writer(myCSVFile, delimiter=';')
    while True:
        naam=input('wat is je naam ')
        if naam =='einde'
            break
        voorl=input('geef je voorletter ')
        gbdatum=input('geef je geboortedatum ')
        email=input('geef je email dares ')
        writer.writerow((voorl,naam,gbdatum,email))

