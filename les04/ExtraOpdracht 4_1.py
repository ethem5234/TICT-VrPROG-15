temp= eval(input('wat is de temperatuur vandaag: '))
if temp <= 0:
    print('Het vries vandaag')
elif temp >0 and temp <= 15:
    print('Het is koud vandaag')
elif temp >15:
    print('Het is lekker vandaag')