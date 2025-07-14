#Grace Estefania Ramos Cortez 240414

#ingresar un numero de 3 digitos
numero = int(input("Ingresa un numero: "))
i = 0

#operacion 
i=i+1
resto = numero % 10
numero = int(numero / 10)
#impresion
print("%d" % (resto), end = "")