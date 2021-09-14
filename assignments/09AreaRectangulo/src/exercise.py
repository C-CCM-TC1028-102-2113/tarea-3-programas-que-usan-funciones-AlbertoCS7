def area (base, altura):
    return (base * altura)

def main():
    #escribe tu código abajo de esta línea
    base = float(input('Dime la base:'))
    altura = float(input('Dime la altura:'))
    area = (base * altura)
    print('El area del rectangulo es:'+ str(area) + ':)')
    pass

if __name__=='__main__':
    main()
