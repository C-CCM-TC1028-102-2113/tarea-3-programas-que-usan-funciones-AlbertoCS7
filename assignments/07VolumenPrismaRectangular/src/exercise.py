def arearectangulo (base, altura):
    area = (base * altura)
    return area

def volumen(area, profundidad):
   volumen = (area * profundidad)
   return volumen

def main():
    #escribe tu código abajo de esta línea

base = float(input('Dime la base:'))
altura = float(input('Dime la altura:'))
profundidad = float(input('Dime la profundidad:'))
    print('El volumen del prisma rectangular es:' +str(volumen))
pass
if __name__=='__main__':
    main()
