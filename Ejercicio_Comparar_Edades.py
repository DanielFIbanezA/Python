#Este es un programa para comparar las edades
miEdad = 23
print("yo tengo una edad de: ", miEdad)
suEdad = int(input("Por favor ingrese su edad: "))

if (suEdad > miEdad):
    print("El es mayor que yo")
elif (suEdad == miEdad):
    print("Los dos tenemos la misma edad")
else:
    print("El es mas joven que yo")
