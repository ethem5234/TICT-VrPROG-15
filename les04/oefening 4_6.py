#programma (wachtwoord, met minstens 6 letters en 2 verschillende wachtwoorden

def new_password(oldpassword,newpassword):
    if oldpassword != newpassword and len(newpassword)>=6 :
       #checkt ook of er een cijfer in de nieuwe wachtwoord zit
        for c in newpassword:
            if c in '0123456789':
             return  True
             return False
    else:
        return False
# methode 2 om te checken of er een cijfer zit in de wachtwoord

#def new_password(oldpassword,newpassword):
#    cijferInp=False
#    for c in newpassword:
#       if c in '0123456789':
#            cijferInP=True
#    if oldpassword != newpassword and len(newpassword) >= 6 and cijferInP:
#        return True

#True
res = new_password('vakProg17','python17')
print(res)
#True
print(new_password('huProg17','huprog17'))
#False
print(new_password('vakProg17','Pro17'))
