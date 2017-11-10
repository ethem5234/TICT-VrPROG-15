
try:
    prijs= 4356

    aantal=eval(input('Hoeveel personen reizen mee?: '))
    p_p=prijs/aantal
    print(p_p)

except ZeroDivisionError:
    print('- Delen door nul kan niet!')
except '-' in aantal:
    print('- Negatieve getallen zijn niet toegestaan!')
