#Grace Estefania Ramos Cortez 240414 
#Algoritmo que suma y promedia 3 numeros 

#solicitar al usuario que ingrese 3 numeros 
num1=float(input("Ingrese el primer numero:"))
num2=float(input("Ingrese el primer numero:"))
num3=float(input("Ingrese el primer numero:"))

#calculae la suma de los numeros 
suma =num1+num2+num3  
prom=suma/3

#imprimir la suma y el promedio 
#f en print significa la contetacion de una variable a un texto
print(f"la suma de los numeros es:{suma}")
print(f"el promedio de los numeros es:{prom}")