print("Este es un programa para calcular el area y la circunferencia de un circulo")
import math
radio = float(input("Por favor ingrese el valor del radio: "))
area = math.pi*(radio**2)
circunferencia = 2*math.pi*radio
print("El area del circulo es : ", round(area,2) )
print("La circunferencia del circulo es : ", round(circunferencia,2))

