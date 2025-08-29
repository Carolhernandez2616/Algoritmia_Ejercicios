#NOMBRE
# Calcular eldescuento de una compra

#ENTRADA
# Compra del valor ingresado por el usuario

#SALIDA
#Si la compra es mayor a 1000, se aplica un 10% de descuento , en caso de lo contrario no se aplicaria descuento

#PROCESO
#Si la compra  > 1000 se aplica el 10% de  descuento ,en caso de lo contrario no se aplicaria descuento
Compra = float(input("Ingrese el valor de su compra:"))
if Compra > 1000 :
     descuento = Compra * 0.10
else:
     descuento = 0
print("El valor de la compra es:" ,Compra)
print("El descuento aplicado es:", descuento)
print("El total a pagar es:",Compra - descuento)

