def arearectangulo (base, altura):
    area = (base * altura)
    return area

def volumen(area, profundidad):
   volumen = (area * profundidad)
   return volumen

def main():
    #escribe tu código abajo de esta línea

    base = float(input('Dime la base:')) ##1. base es una variable que solo existe en el entorno de la función main
    altura = float(input('Dime la altura:')) ##2. altura es una variable que solo existe en el entorno de la función main
    profundidad = float(input('Dime la profundidad:'))
    #area = arearectangulo(base, altura)
    #volumen = (area, profundidad)
    print('El volumen del prisma rectangular es:' +str(volumen))     
if __name__=='__main__':
    main()
