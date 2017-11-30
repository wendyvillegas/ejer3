print("1. Area del circulo")
print("2. Area del cuadrado")
print("3. Area del triangulo")
print("HELOOOOO")
opcion=int(input(print("Ingrese la opcion")))



def circulo(radio):
    area=(radio*radio)*3.1415
    return area

if opcion==1:
    radio=int(input(print("Ingrese el radio")))
    total= circulo(radio)
