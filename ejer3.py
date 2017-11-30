def circulo(radio):
    area=(radio*radio)*3.1415
    return area

def cuadrado(lado):
    area=(lado*lado)
    return area

def triangulo(alturaa, basee):
    res = (base* alturaa)/2
    return res


print("1. Area del circulo")
print("2. Area del cuadrado")
print("3. Area del triangulo")
opcion = int(input("Ingrese la opcion:   "))



if opcion == 1:
    radio=int(input("Ingrese el radio:  "))
    total= circulo(radio)

if opcion==2:
    lado=int(input("Ingrese el lado:  "))
    total=cuadrado(lado)

if opcion == 3:
    altura = float (input("Ingrese la ALTURA del triangulo: "))
    base = float(input("Ingrese la BASE del triangulo: "))
    triangulo(altura, base)
    print("EL AREA ES: " + str(triangulo(altura, base)))
    
    
    
    

