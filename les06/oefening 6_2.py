dieren = ['hond',' kat',' vogel',' leeuw',' olifant',' beer',' koe',' schaap']
for dier in dieren:
    print(dier)

#met een rangefunctie

for i in range(0,8): # print i werkt niet want dan print die de index en print dieren kent die niet
    print(dieren[i]) # print de i index in lijst dieren
for i in range(len(dieren)):
    print(dieren[i])