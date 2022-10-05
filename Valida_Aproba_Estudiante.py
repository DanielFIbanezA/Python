nota1 = float (input("Escriba la nota 1: "))
nota2 = float (input("Escriba la nota 2: "))
ausencias = float (input("Escriba el numero de faltas a clase: "))
total_clases = int (input("Escriba el numero total de clases: "))

prom_notas = (nota1 + nota2)/2
asistencia = (((total_clases - ausencias)/total_clases)*100)

if (prom_notas >= 6):
    if (asistencia >= 80):
        print("El estudiante ha aprobado satisfatoriamente con un promedio de: ",prom_notas," de 10 y una asistencia a clases de: ", asistencia,"%" )
    else:
        print("El estudiante no aprobo por fallas: ", ausencias, "fallas de ", total_clases)
else:
    print("El estudiante obtuvo un promedio inferior a 6 y no aprueba")
