#Eeste deel

def convert(ce):
    fa = ce * 1.8 + 32
    return fa

# deel 2
def table():
    for temp in range(-30,40,10):
        print('{:9} {:1}'.format(temp, convert(temp))