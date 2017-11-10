gewicht= eval(input('wat is je gewicht in kilos: '))
lengte=  eval(input('wat is je lengte in meters: '))
BMI= gewicht//(lengte**2)

if BMI <=18.5:
    print('je hebt ondergewicht')
elif BMI>18.5 and BMI<=25:
    print('je hebt normaal gewicht')
else:
    print('je hebt overgewicht')