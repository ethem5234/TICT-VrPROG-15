def ticker():
    infile=open('ticker.txt','r')
    regels= infile.readlines()
    infile.close()
    tickerdict={}
    for regel in regels:
        tickerregel = regel.split(':')
        sleutel=tickerregel[0]
        waarde= tickerregelegel[1].split()
        tickerdict[sleutel]=waarde
        return tickerdict
ticker()