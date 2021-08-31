def bisiesto(año):
    if año%100==0 and año%400!=0:
        return 'No es bisiesto :('
    elif año%4==0 and a%100!=0:
        return 'Si es bisiesto :)'
    
def main():
    #escribe tu código abajo de esta línea
    año = int(input('Dime el año:'))
    comprobacion = bisiesto(año)
    print(comprobacion)
    pass

if __name__=='__main__':
    main()
