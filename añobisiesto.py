#NOMBRE
#Verificador de un año BISIESTO

#ENTRADA
#Año ingresado por el usuario 

#SALIDA
#Verificar si el año es BISIESTO

#PROCESO
#Calcula  si el año es BISIESTO si el multiplo es 4
#AUTOR

AñoBisiesto = int(input("Ingrese un año:"))
if AñoBisiesto % 4 == 0 and AñoBisiesto % 100 != 0 or AñoBisiesto % 400 == 0:
   print("El año es BISIESTO.")
else:
   print("El año no es BISIESTO.")
   
    

