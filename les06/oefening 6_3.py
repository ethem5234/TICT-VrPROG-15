zin= input('Voer een zin in: ')
woorden= zin.split()
acroniem= ''
for letter in woorden:
    acroniem= acroniem +(letter[0].upper())

print(acroniem)