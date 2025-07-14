#Grace Estefania Ramos Cortez 240414
#& Todos los lunes, miercoles y viernes,una persona corre la misma ruta y cronometra su tiempo 
#obtener el promedio de su tiempo de una semana

dia1=float(input("Ingrese el tiempo del dia lunes "))
dia2=float(input("Ingrese el tiempo del dia Miercoles "))
dia3=float(input("Ingrese el tiempo del dia Viernes"))

#operaciones 
prom=(dia1+dia2+dia3)/3

#Imprimir
print(f"El dia lunes su tiempo fue de {dia1}")
print(f"El dia Miercoles su tiempo fue de {dia2}")
print(f"El dia Viernes su tiempo fue de {dia3}")
print(f"El promedio de su semana fue de {prom}")