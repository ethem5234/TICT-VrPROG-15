def seizoen(maand):
    if maand == 12 or 1 or 2:
        print('Het is winter')
    elif maand == 3 or 4 or 5:
        print('Het is lente')
    elif maand == 6 or 7 or 8:
        print('Het is zomer')
    elif maand == 9 or 10 or 11:
        print('Het is herft')

maand= eval(input('voer een maand in: '))
print(seizoen(maand))