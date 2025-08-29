#NOMBRE
#Verificar la mayoria de edad

#ENTRADA
#Año de nacimiento ingresado por el usuario

#SALIDA
#Mostrar si es mayor de edad o menor

#PROCESO
#Calcular si es mayor de edad  >= 18 o menor de edad

añoNacimiento = int(input("Ingrese su año de nacimiento: "))
añoActual = 2025
edad = añoActual - añoNacimiento
if edad >= 18:
    print("Tienes", edad, "años. Eres mayor de edad.")
else:
    print("Tienes", edad, "años. Eres menor de edad.")