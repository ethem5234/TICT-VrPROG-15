while True:
    woord= input('Geef een woord: ')
    if len(woord)==4:
        print('inlezen van een correcte string: {}'.format(woord))
        break
    else:
        print('{} heeft {} letters'.format(woord,len(woord)))