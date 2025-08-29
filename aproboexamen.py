#NOMBRE
#Verificar la aprobación del examen

#ENTRADA
# Nota ingresada por el usuario

#SALIDA
# Mostrar si el estudiante Aprobó o Reprobó

#PROCESO
#Comprobar si el estudiante aprobo >= 60 o reprobo 

Nota = float(input("Ingrese su nota:"))
if Nota >= 60:
    print("El estudiante APROBÓ.")
else:
    print("El estudiante REPROBÓ.")