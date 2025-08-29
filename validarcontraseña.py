#NOMBRE
#Verificador de contraseña

#ENTRADA
#Contraseña ingresada por el usuario

#SALIDA
#Mostrar si la contraseña es permitida o denegada

#PROCESO
#Comprobar si la contraseña es permitida o denegada

Contraseña = str(input("Ingrese la contraseña:"))

if Contraseña == "clave123":
  print("Acceso permitido.")
else:
  print("Acceso denegado.")