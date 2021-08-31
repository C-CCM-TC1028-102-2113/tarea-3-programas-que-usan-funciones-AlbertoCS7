def maximo(pliegos, plu):
    if pliegos< plumones:
        return (pliegos * 12)
    elif pliegos>plumones:
        return (plumones * 35)
    
def main():
    #escribe tu código abajo de esta línea
    
pliegos = int(input('Dame el número de papeles:'))
plumones = int(input('Dame el número de plumones:'))
tarjetas = maximo(pliegos, plumones)
    print('El número máximo de tarjetas españolas que se pueden hacer es:'+ str(tarjetas))
pass

if __name__=='__main__':
    main()
