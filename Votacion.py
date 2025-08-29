#NOMBRE
#Verifica tu año de nacimiento,edad actual

#ENTRADA
#Edad ingresado por el usuario

#SALIDA
#Mostrar si eres mayor de edad o menor ,para comprobar si puede o no votar

#PROCESO
#Calcular si eres mayor o menor de edad para votar 


año =int(input("Ingresa tu edad:"))
 
if año >= 18:
    print("Eres mayor de edad, puedes votar")
else:
    print("Eres menor de edad, no puedes votar")
