#NOMBRE
#Verificar si el triangulo es equilatero

#ENTRADA
# Tres números ingresados por el usuario

#SALIDA
#Mostrar  si el triangulo es equlatero o no 

#PROCESO
#Comprobar si el triangulo es equilatero o no

lado1 = float(input("Ingresa un numero:"))
lado2 = float(input("Ingresa el segundo numero:"))
lado3 = float(input("Ingresa el tercer numero:"))


if lado1 == lado2 and lado2 == lado3:
  print("El triangulo es EQUILATERO:")
else:
  print("El triangulo NO es EQUILATERO:")