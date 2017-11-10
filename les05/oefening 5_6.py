infile= open ('kaartnummers.txt', 'r')
regels= infile.readlines()
infile.close()
#ik open een file die leeg is die kaartnummersuit.txt heet waarin ik ga schrijven, dat doe je met outfile =
outfile= open('kaartnummersuit.txt', 'w')
for regel in regels:
    kaartinfo = regel.split(',')
    outfile.write('{} heeft kaartnummer:{}\n'.format(kaartinfo[1].strip(),kaartinfo[0])) #file modus is nu 'w' in plaats van 'r'
outfile.close()