meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
birthday = input("Ingrese su fecha de cumpleaños con el siguiente formato, DD-MM-YYYY: ")
mesCumpleaños = int(birthday[3:5]) - 1
bd_mes= meses[mesCumpleaños]
print("Usted nacio en el mes de: " , bd_mes)

