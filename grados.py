#NOMBRE
#Verificar los grados de la temperatura

#ENTRADA
#Número de temperatura ingresada por el usuario

#SALIDA
#Mostrar si la temperatura  es adecuada o no

#PROCESO
#Calcular si la temperatura <= 0 es adecuada o no para congelar
numero1 = int(input("Ingrese temperatura:"))
if numero1 <= 0:
  print ("C° Temperatura adecuada para congelar.")
else:
  print ("C° Temperatura no adecuada para congelar.")
