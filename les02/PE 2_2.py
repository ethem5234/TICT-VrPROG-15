cijferICOR= 6.5
cijferPROG= 7
cijferCSN= 7.5
gemiddelde= (cijferICOR+cijferPROG+cijferCSN)/2
beloning= (cijferCSN*30)+(cijferPROG*30)+(cijferICOR*30)
overzicht= 'Mijn cijfers '+str('gemiddelde')+'leveren een beloning van € '+str(beloning)+' op!'
print(overzicht)