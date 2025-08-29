#NOMBRE
#Verificar el  permiso  del sistema

#ENTRADA
#Rol ingresado por el usuario

#SALIDA
#Mostrar si el  acceso  es permitido o denegado

#PROCESO
#Calcular si con la clave el acceso es permitido o denegado
rol = str(input("Ingrese su rol Admin / Usuario:"))
if rol == "Admin":
  print("Acceso permitido:")
else:
  print("Acceso denegado:")