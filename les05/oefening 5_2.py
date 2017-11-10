s='voorbeeld'
#eerste letter word hoofdletter
print(s.capitalize())
print(s)
#de aantal e's worden geteld in variable s
print(s.count('e'))
#de plaats van de eerste e in variable s word weergeven
print(s.find('e'))
#hij vervangs alle e's in variable s in een a
print(s.replace('e','a'))
s1='Voorbeeld'
#hij maakt alle letters van de sting in s in kleine letters
print(s1.lower())
#hij veranderd alle letters in hoofdletters
print(s1.upper())
#hij maakt van de variable een list
s2= 'dit is een voorbeeld'
print(s2.split())
#als er geen spatie is (geen element) paat die van de variable 1 list item
s3='dit-is-een-voorbeeld'
print(s3.split())
#als je tussen de quotes een teken zet beteken dit dat op de plaats van deze teken de list een nieuwe list item splitst
print(s3.split('-'))
woord='Eenheelerglangwoord'
