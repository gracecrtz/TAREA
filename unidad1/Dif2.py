#Grace Estefania Ramos Cortez 240414

#hacer un programa que invierta los números de una variable de dos dígitos.


N=float(input("Escribe el numero de dos digitos"))

#operaciones 



D1= N // 10
D2=N % 10*10

res=D2+D1

#imprimir

print(f"la inversion de {N } es {res}")  