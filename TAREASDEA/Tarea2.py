#Crear el arreglo 
Datos = [10, 15, 21, 34, 44, 50, 66, 75, 80, 99, 100]
n = len(Datos)


Meta = 75

#Establecer lso pasos y crear un indice 
pasos = 0
ubicacion_indice = -1

inicio = 0 
final = n - 1


# While para detectar la complejidad de log 
limite_log = 0
temp_n = n
while temp_n > 0:
    temp_n = temp_n // 2
    limite_log += 1

#Crear un algoritmo si detecte la complejidad 
#Hay qeu crear un contador de pasos 
while inicio <= final :
    pasos += 1
    micha = (inicio + final) // 2

    if Datos[micha] == Meta:
        ubicacion_indice = micha 
        break
    elif Datos[micha] < Meta :
        inicio = micha + 1
    else :
        final = micha - 1

print(" El resultado del analsis ")            
if ubicacion_indice != -1:
    print("Meta encontrada en indice:", ubicacion_indice)
else:
    print("Meta no encontrada")

print("Pasos totales:", pasos)



print("\n--- Clasificación de Notación Big O ---")

if pasos == 1:
    print("Orden: O(1) - Constante")
    
elif pasos <= limite_log:
    print("Orden: O(log n) - Logarítmica")
    print("Explicación: Los pasos son menores o iguales al limite de divisiones del arreglo.")

elif pasos <= n:
    print("Orden: O(n) - Lineal")

else:
    print("Orden: O(n^2) - Exponencial")

print("---------------------------------------")