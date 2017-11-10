def lang_genoeg(lengte):
    if lengte>=120:
        return('Je bent lang genoeg voor de atractie!')
    else:
        return('Sorry, je bent de klein!')

lengte= eval(input('Wat is je lengte: '))
print(lang_genoeg(lengte))