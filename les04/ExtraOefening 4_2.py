temp = eval(input('Wat is de tempratuur vandaag: '))

def geef_melding(temp):
    if temp <= 0:
        print('Het vries vandaag')
    elif temp > 0 and temp <= 15:
        print('Het is koud vandaag')
    elif temp > 15:
        print('Het is lekker vandaag')
geef_melding(temp)
