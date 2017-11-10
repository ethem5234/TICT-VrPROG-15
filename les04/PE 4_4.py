def new_password(oldpassword,newpassword):
    if oldpassword != newpassword and len(newpassword)>=6 :
       #checkt ook of er een cijfer in de nieuwe wachtwoord zit
        for c in newpassword:
            if c in '0123456789':
             return  True
             return False
    else:
        return False