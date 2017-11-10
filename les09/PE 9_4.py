import  csv
with open('artikel.csv','w',newline='') as myCSVFile:
    writer= csv.writer(myCSVFile,delimiter=';')
    writer.writerow(('artikelnummer','artikelcode'))
    while True:
        artikelnummer=input('wat is het artikelnummer')
        if artikelnummer == '':
            break
        artikelcode=input('wat is de artikelcode?')
        writer.writerow((artikelnummer,artikelcode))