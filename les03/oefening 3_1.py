naam = input('Wat is je naam?: ')
leeftijd= eval(input('Wat is je leeftijd?: '))

if leeftijd<18:
    print(naam+', je mag nog niet stemmen.')
else:
    print(naam+', je mag stemmen.')