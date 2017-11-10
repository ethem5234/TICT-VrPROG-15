#hoe maak je een lijst van een file

infile= open('oefening 5_5.txt', 'r')
inhoud1= infile.read()
infile.close()
inhoud2= inhoud1.split()
print(inhoud2)
#file openen en toekennen aan een file object
infile= open('oefening 5_5.txt', 'r')



