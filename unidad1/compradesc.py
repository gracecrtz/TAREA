#GraceEstefania Ramos Cortez 240414
#Algoritmo que calcula el descuento de una compra 

#Ingresar los valores 
compra=float(input("Ingrese el valor de la compra: "))
porcentaje=float(input("Ingrese el valor de el descuento: "))

#Operaciones 
final=(compra*porcentaje)/100
resul=compra-final

#imprimir resultado 
print(f"La compra de {compra:.0f} con el descuento {porcentaje:.0f} % da como precio final {resul:.0f}")

