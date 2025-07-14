#Grace Estefania Ramos Cortez 240414 
#Algoritmo que calcula las operaciones basicas (+,- ,*,/) de dos numeros

#Ingresa dos numeros 
#input es para ingresar el texto cuando vayas a pedir una variable
x=float(input("Ingrese el primer numero: "))
y=float(input("Ingrese el segundo numero: "))

#operaciones 
sum=x+y
res=x-y
mul=x*y
div=x/y

#impresion de las operaciones
#:.Nf es los numeros que saldran despues del punto(N=cualquier numero)
print(f"la suma de los numeros {x:.0f} {y:.0f} es:{sum:.0f}")
print(f"la resta de los numeros {x:.0f} {y:.0f} es:{res:.0f}")
print(f"la multiplicacion de los numeros {x:.0f} {y:.0f} es:{mul:.0f}")
print(f"la division de los numeros {x:.0f} {y:.0f} es:{div:.0f}")


